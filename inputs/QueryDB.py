class QueryDB:
	def __init__(self):
		
		from datetime import datetime
		from datetime import timedelta
		from objects import Asset, Skill, Manpower
		from objects.Schedule import Schedule
		from objects.Task import Task
		from objects.DateRange import DateRange
		from pyodbc import connect
		
		self.name = 'QueryDB'
		_now = datetime.now()
		_window = 30 #days
		_maxAssetsInWork = 2
		_platform = 1 #E-6
		_hardware = 5765 #aircraft
		_asset = 162782 #TODO: remove
		_unit = 4 #Days
		
		schedule = Schedule(self.name, DateRange(_now, _now + timedelta(days=_window)), _maxAssetsInWork)

		cnxn = connect('DRIVER={SQL Server};SERVER=;DATABASE=;UID=;PWD=')
		cursor = cnxn.cursor()
		
		assets = {}
		for r in cursor.execute("SELECT id, name, serviceStartDate FROM EndItem WHERE platformId = ? AND hardwareId = ? AND id = ?", _platform, _hardware, _asset):
			assets[r.id] = Asset(r.id, r.name, r.serviceStartDate)
		
		skills = {}
		for r in cursor.execute("SELECT id, name, available, 8 hoursPerDay FROM Skill WHERE platformId = ?", _platform):
			skills[r.id] = Skill(r.id, r.name, r.available, r.hoursPerDay)
			
		tasks = {}
		for r in cursor.execute("""
			SELECT	t.id, 
					t.[description] name, 
					t.unitId unit, 
					t.threshold, 
					CAST(t.taskInterval AS INT) interval, 
					ISNULL((
						SELECT	'Manpower('+ CAST(x.id AS VARCHAR(MAX)) + ',skills[' + CAST(x.skillId AS VARCHAR(MAX)) + '],' + CAST(x.taskTime AS VARCHAR(MAX)) + ') ' AS [text()]  
						FROM	Manpower x
						WHERE	x.taskId = t.id
						FOR XML PATH('')
					),'') manpowers, 
					ISNULL((
						SELECT	CAST(x.preReqTaskId AS VARCHAR(MAX)) + ' ' AS [text()]  
						FROM	PreReqTaskLink x
						WHERE	x.taskId = t.id
						FOR XML PATH('')
					),'') pre, 
					ISNULL((
						SELECT	CAST(x.assocTaskId AS VARCHAR(MAX)) + ' ' AS [text()]  
						FROM	AssocTaskLink x
						WHERE	x.taskId = t.id
						FOR XML PATH('')
					),'') concurrent, 
					ISNULL((
						SELECT	CAST(x.postReqTaskId AS VARCHAR(MAX)) + ' ' AS [text()]  
						FROM	PostReqTaskLink x
						WHERE	x.taskId = t.id
						FOR XML PATH('')
					),'') post, 
					ISNULL((
						SELECT	CAST(x.taskId AS VARCHAR(MAX)) + ' ' AS [text()]  
						FROM	TaskConfiguration x
						WHERE	x.configurationId IN (
							SELECT	cc.configurationIdConflict
							FROM	ConfigurationConflict cc
							WHERE	cc.configurationId IN (
								SELECT	tc.configurationId
								FROM	TaskConfiguration tc
								WHERE	tc.taskId = t.id
							)
						)
						GROUP BY x.taskId
						FOR XML PATH('')
					),'') conflict, 
					NULL maximums, 
					t.startDate [start], 
					t.endDate [end]
			FROM	Task t
			WHERE	t.active = 1
			AND		t.platformId = ?
			AND		t.unitId = ?
		""", _platform, _unit):
			_manpowers = []
			for x in r.manpowers.split(): 
				_manpowers.append(eval(x))
			tasks[r.id] = Task(
							id=r.id, 
							name=r.name, 
							unit=r.unit, 
							threshold=r.threshold, 
							interval=r.interval, 
							manpowers=_manpowers, 
							tasks={ 'pre':r.pre.split(), 'concurrent':r.concurrent.split(), 'post':r.post.split(), 'conflict':r.conflict.split() },
							maximums=[],
							dateRange=DateRange(r.start, r.end).intersection(schedule.dateRange)
						)

		for r in cursor.execute("""
			DECLARE @platformId INT
			SET @platformId = ?
			DECLARE @unitId INT
			SET @unitId = ?
			DECLARE @hardwareId INT
			SET @hardwareId = ?
			DECLARE @endItemId INT
			SET @endItemId = ?
			
			SELECT endItemId, taskId, [end]
			FROM	(
				SELECT	et.endItemId, et.taskId, ISNULL(et.completed, e.endDate) [end]
				FROM	EventTaskLink et
					INNER JOIN [Event] e ON e.id = et.eventId
				WHERE	et.endItemId IN (SELECT id FROM EndItem WHERE platformId = @platformId AND hardwareId = @hardwareId)
				AND		et.taskId IN (SELECT id FROM Task WHERE active = 1 AND platformId = @platformId AND unitId = @unitId)
				AND		(et.locked = 1 OR et.sequenceOverride = 1 OR et.percentComplete <> 0)
				AND		et.endItemId = @endItemId
			) x
			WHERE	[end] >= GETDATE()
				UNION
			SELECT endItemId, taskId, MAX([end])
			FROM	(
				SELECT	et.endItemId, et.taskId, ISNULL(et.completed, e.endDate) [end]
				FROM	EventTaskLink et
					INNER JOIN [Event] e ON e.id = et.eventId
				WHERE	et.endItemId IN (SELECT id FROM EndItem WHERE platformId = @platformId AND hardwareId = @hardwareId)
				AND		et.taskId IN (SELECT id FROM Task WHERE active = 1 AND platformId = @platformId AND unitId = @unitId)
				AND		et.endItemId = @endItemId
			) x
			WHERE	[end] < GETDATE()
			GROUP BY endItemId, taskId
			""", _platform, _unit, _hardware, _asset):
			schedule.force(assets[r.endItemId], tasks[r.taskId], DateRange(r.end, r.end))	

		self.assets = assets.values()
		self.tasks = tasks.values()		
		self.schedule = schedule

DECLARE @platformId INT
SET @platformId = 1
DECLARE @hardwareId INT
SET @hardwareId = 5765


--Assets
SELECT 	'' + CAST(id AS NVARCHAR(MAX)) + ': Asset(' + CAST(id AS NVARCHAR(MAX)) + ', ''' + name + ''', datetime(' + CAST(YEAR(serviceStartDate) AS NVARCHAR(MAX)) + ', ' + CAST(MONTH(serviceStartDate) AS NVARCHAR(MAX)) + ', ' + CAST(DAY(serviceStartDate) AS NVARCHAR(MAX)) + ')),' 
FROM 	EndItem 
WHERE	platformId = @platformId  AND id = 164410

--Skills
SELECT 	'' + CAST(id AS NVARCHAR(MAX)) + ': Skill(' + CAST(id AS NVARCHAR(MAX)) + ', '''+name+''', ' + CAST(available AS NVARCHAR(MAX))+', 8),' 
FROM 	Skill 
WHERE	platformId = @platformId

--Tasks TODO: Only show conflicts with tasks in query
DECLARE @unitUsage TABLE (unitId INT, usageAmount FLOAT)

INSERT INTO @unitUsage (unitId, usageAmount)
SELECT	unitId, AVG(usageAmount)
FROM	PlannedUsage
WHERE	unitId IN (
	SELECT	id
	FROM	Unit
	WHERE	platformId = @platformId
)
GROUP BY unitId

SELECT ''+CAST(id AS NVARCHAR(MAX))+': Task(
				id='+CAST(id AS NVARCHAR(MAX))+', 
				name='''+ISNULL(name,'')+''', 
				unit=0, 
				threshold='+ISNULL(CAST(CEILING(threshold / usageUnit) AS NVARCHAR(MAX)),'0')+', 
				interval='+ISNULL(CAST(FLOOR(interval / usageUnit) AS NVARCHAR(MAX)),'0')+', 
				manpowers=['+ISNULL(LEFT(manpowers,LEN(manpowers)-1),'')+'], 
				conflicts=['+ISNULL(LEFT(conflict,LEN(conflict)-1),'')+'],
                totalTasks=2236
			),'
FROM (
	SELECT	t.id, 
            t.[description] name, 
            t.unitId unit, 
			(SELECT usageAmount FROM @unitUsage WHERE unitId =  t.unitId) usageUnit,
            t.threshold, 
            t.taskInterval interval, 
            (
                SELECT    'Manpower('+ CAST(x.id AS VARCHAR(MAX)) + ',skills[' + CAST(x.skillId AS VARCHAR(MAX)) + '],' + CAST(ISNULL(x.taskTime,0) AS VARCHAR(MAX)) + '),' AS [text()]  
                FROM    Manpower x
                WHERE    x.taskId = t.id
                FOR XML PATH('')
            ) manpowers, 
            (
				SELECT    CAST(x.taskId AS VARCHAR(MAX)) + ',' AS [text()]  
				FROM    TaskConfiguration x
				WHERE    x.configurationId IN (
					SELECT    cc.configurationIdConflict
					FROM    ConfigurationConflict cc
					WHERE    cc.configurationId IN (
						SELECT    tc.configurationId
						FROM	TaskConfiguration tc
						WHERE    tc.taskId = t.id
					)
				)
				AND		x.taskId IN (SELECT id FROM Task WHERE active = 1 AND t.platformId = @platformId)
				GROUP BY x.taskId
				FOR XML PATH('')
            ) conflict, 
            NULL maximums, 
            t.startDate [start], 
            t.endDate [end]
    FROM    Task t
    WHERE	t.active = 1
    AND		t.platformId = @platformId
) x

--History/Locked
SELECT 'schedule.force(assets[' + CAST(endItemId AS VARCHAR(MAX)) + '], tasks[' + CAST(taskId AS VARCHAR(MAX)) + '], DateRange(datetime('+CAST(YEAR([end]) AS VARCHAR(MAX))+', '+CAST(MONTH([end]) AS VARCHAR(MAX))+', '+CAST(DAY([end]) AS VARCHAR(MAX))+'), datetime('+CAST(YEAR([end]) AS VARCHAR(MAX))+', '+CAST(MONTH([end]) AS VARCHAR(MAX))+', '+CAST(DAY([end]) AS VARCHAR(MAX))+')))'
FROM (
	SELECT endItemId, taskId, [end]
	FROM    (
		SELECT    et.endItemId, et.taskId, ISNULL(et.completed, e.endDate) [end]
		FROM    EventTaskLink et
			INNER JOIN [Event] e ON e.id = et.eventId
		WHERE    et.endItemId IN (SELECT id FROM EndItem WHERE platformId = @platformId AND hardwareId = @hardwareId)
		AND        et.taskId IN (SELECT id FROM Task WHERE active = 1 AND platformId = @platformId)
		AND        (et.locked = 1 OR et.sequenceOverride = 1 OR et.percentComplete <> 0)
	) x
	WHERE    [end] >= GETDATE()
		UNION
	SELECT endItemId, taskId, MAX([end])
	FROM    (
		SELECT    et.endItemId, et.taskId, ISNULL(et.completed, e.endDate) [end]
		FROM    EventTaskLink et
			INNER JOIN [Event] e ON e.id = et.eventId
		WHERE    et.endItemId IN (SELECT id FROM EndItem WHERE platformId = @platformId AND hardwareId = @hardwareId)
		AND        et.taskId IN (SELECT id FROM Task WHERE active = 1 AND platformId = @platformId)
	) x
	WHERE    [end] < GETDATE()
	GROUP BY endItemId, taskId
) x
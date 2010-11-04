class Simple:
	def __init__(self):
		
		from datetime import datetime
		from objects import Asset, Skill, Manpower
		from objects.Schedule import Schedule
		from objects.Task import Task
		from objects.DateRange import DateRange
		
		self.name = 'Simple'
		
		schedule = Schedule(self.name, DateRange(datetime(2010, 1, 1), datetime(2010, 2, 1)), 2)
		
		assets = {
			1: Asset(1, 'Airplane', datetime(2010, 1, 1)),
			2: Asset(2, 'Tank', datetime(2010, 1, 1)),
			3: Asset(3, 'Truck', datetime(2010, 1, 1))
		}
		
		skills = {
			1: Skill(1, 'Electrician', 5, 8),
			2: Skill(2, 'Mechanic', 10, 8),
			3: Skill(3, 'Painter', 1, 8)
		}
		
		tasks = {
			1: Task(
				id=1, 
				name='Change Oil', 
				unit=1, 
				threshold=5, 
				interval=10, 
				manpowers=[
					Manpower(1, skills[1], 1), 
					Manpower(2, skills[2], 4), 
					Manpower(3, skills[2], 2)
				], 
				tasks={ 'pre':[], 'concurrent':[], 'post':[], 'conflict':[2] },
				maximums=[],
				dateRange=DateRange(datetime(2010, 1, 2), None).intersection(schedule.dateRange)
			),
			2: Task(
				id=2, 
				name='Paint', 
				unit=1, 
				threshold=5, 
				interval=20, 
				manpowers=[
					Manpower(4, skills[3], 20)
				], 
				tasks={ 'pre':[], 'concurrent':[], 'post':[], 'conflict':[1] },
				maximums=[{ 'type':'FY', 'max':1, 'key':2010, 'value':0 }],
				dateRange=DateRange(None, None).intersection(schedule.dateRange)
			),
			3: Task(
				id=3, 
				name='Rotate Tires', 
				unit=1, 
				threshold=5, 
				interval=20, 
				manpowers=[
					Manpower(5, skills[2], 4)
				], 
				tasks={ 'pre':[], 'concurrent':[1], 'post':[], 'conflict':[2] },
				maximums=[],
				dateRange=DateRange(None, None).intersection(schedule.dateRange)
			),
			4: Task(
				id=4, 
				name='Check Tires', 
				unit=None, 
				threshold=None, 
				interval=None, 
				manpowers=[
					Manpower(6, skills[2], 1)
				], 
				tasks={ 'pre':[], 'concurrent':[], 'post':[], 'conflict':[2] },
				maximums=[],
				dateRange=DateRange(None, None).intersection(schedule.dateRange)
			)
		}
		
		
		#schedule.force(assets[1], tasks[1], DateRange(datetime(2010, 1, 1), datetime(2010, 1, 1)))
		schedule.force(assets[1], tasks[2], DateRange(datetime(2010, 1, 1), datetime(2010, 1, 1)))
		schedule.force(assets[2], tasks[1], DateRange(datetime(2010, 1, 1), datetime(2010, 1, 1)))
		schedule.force(assets[2], tasks[2], DateRange(datetime(2010, 1, 1), datetime(2010, 1, 1)))
		schedule.force(assets[3], tasks[1], DateRange(datetime(2010, 1, 1), datetime(2010, 1, 1)))
		schedule.force(assets[3], tasks[2], DateRange(datetime(2010, 1, 1), datetime(2010, 1, 1)))
		

		self.assets = assets.values()
		self.tasks = tasks.values()		
		self.schedule = schedule
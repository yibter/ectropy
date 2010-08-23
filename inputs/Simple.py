class Simple:
	def __init__(self):
		
		from datetime import date
		from objects import Asset, Skill, Manpower
		from objects.Schedule import Schedule
		from objects.Task import Task
		from objects.DateRange import DateRange
		
		self.name = "Simple"
		
		schedule = Schedule(self.name, DateRange(date(2010, 1, 1), date(2010, 2, 1)), 2)
		
		assets = {
			1: Asset(1, 'Airplane', date(2010, 1, 1)),
			2: Asset(2, 'Tank', date(2010, 1, 1)),
			3: Asset(3, 'Truck', date(2010, 1, 1))
		}
		
		skills = {
			1: Skill(1, 'Electrician', 5, 8),
			2: Skill(2, 'Mechanic', 10, 8),
			3: Skill(3, 'Painter', 1, 8)
		}
		
		tasks = {
			1: Task(1, 'Change Oil', 1, 5, 10, [
					Manpower(1, skills[1], 1), 
					Manpower(2, skills[2], 4), 
					Manpower(3, skills[2], 2)
				], [2]),
			2: Task(2, 'Paint', 1, 5, 20, [
					Manpower(4, skills[3], 20)
				], [1])
		}
		
		
		#schedule.force(assets[1], tasks[1], DateRange(date(2010, 1, 1), date(2010, 1, 1)))
		schedule.force(assets[1], tasks[2], DateRange(date(2010, 1, 1), date(2010, 1, 1)))
		schedule.force(assets[2], tasks[1], DateRange(date(2010, 1, 1), date(2010, 1, 1)))
		schedule.force(assets[2], tasks[2], DateRange(date(2010, 1, 1), date(2010, 1, 1)))
		schedule.force(assets[3], tasks[1], DateRange(date(2010, 1, 1), date(2010, 1, 1)))
		schedule.force(assets[3], tasks[2], DateRange(date(2010, 1, 1), date(2010, 1, 1)))
		

		self.assets = assets.values()
		self.tasks = tasks.values()		
		self.schedule = schedule
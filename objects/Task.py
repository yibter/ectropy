class Task:
    def __init__(self, id, name, unit, threshold, interval, manpowers, tasks, maximums, dateRange):
        self.id = id
        self.name = name
        self.unit = unit
        self.threshold = threshold
        self.interval = interval
        self.manpowers = manpowers
        self.tasks = tasks
        self.maximums = maximums
        self.dateRange = dateRange
        self.locked = False
        self.hoursPerDay = 8 #TODO: Don't hard-code
        self.relativeWeight = 0 #init value
        self.skills = [] #init value
        self.days = 0 #init value
        self.manhours = 0 #init value
        self.totalAvailableHours = 0 #init value
        if len(manpowers): self.precal() #TODO: Should come from sequencing
        
    def next(self, asset, date):
        #TODO: Add usage units
        #TODO: Add task start/end
        if date == None: return self.addDays(asset.start, self.threshold)
        return max(self.addDays(date, self.interval), self.addDays(asset.start, self.threshold))
        # without rebasing it would be: return self.addDays(date, self.interval) 

    #calculate end date based on start date plus number of days task takes 
    def end(self, start):
        return self.addDays(start, self.days)
         
    def calcDateRange(self, date):
        from objects.DateRange import DateRange
        self.dateRange = DateRange(date, self.end(date))
    
    def addDays(self, date, days):
        from datetime import timedelta
        days -= 1
        return date + timedelta(days=round(days)) #todo: decrement precision if decimal
    
    def precal(self):
        import math
        for manpower in self.manpowers:
            self.days = math.ceil(max(self.days, manpower.hours / (manpower.skill.hoursPerDay *1.0))) #TODO: Don't hard-code
            self.sumSkills(manpower)
            self.manhours += manpower.hours
            self.totalAvailableHours += manpower.skill.availableHours
        #calculate a task weight based on size and availability
        self.relativeWeight = self.manhours / (self.totalAvailableHours *1.0) #TODO: Don't hard-code
    
    def sumSkills(self, manpower):
        newSkill = manpower.skill.copy()
        for _skill in self.skills:
            if newSkill.id == _skill.id:
                _skill.total += manpower.hours
                return
        newSkill.total = manpower.hours
        self.skills.append(newSkill)
    
    def copy(self):
        from copy import deepcopy
        return deepcopy(self)
    
    def schedule(self, date):
        _task = self.copy()
        _task.calcDateRange(date) #Calculate/set date range
        return _task
    
    def forceSchedule(self, dateRange):
        _task = self.copy()
        _task.dateRange = dateRange
        _task.locked = True
        return _task

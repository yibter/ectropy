class Schedule:
    def __init__(self, dateRange, maxAssetsInWork):
        self.dateRange = dateRange
        self.maxAssetsInWork = maxAssetsInWork
        self._schedule = {}     #dateRange >> assets >> tasks

    def force(self, asset, task, dateRange):
        self._addToSchedule(asset, task.forceSchedule(dateRange))

    def blocked(self, asset, task, date):
        _task = task.schedule(date) #Create scheduled task (prevent threading issues)
        if(self._assetAvailabilityFilled(_task.dateRange, asset)): return True
        if(self._skillAvailabilityFilled(_task)): return True
        return False

    def add(self, asset, task, date):
        _task = task.schedule(date) #Create scheduled task
        self._addToSchedule(asset, _task)
        return _task.dateRange.end

    def last(self, asset, task):
        for _task in self._schedule[asset.id]:
            if _task.id == task.id:
                return _task.dateRange.end
    
    def _addToSchedule(self, asset, task):
        if asset.id not in self._schedule: 
            self._schedule[asset.id] = []
        self._schedule[asset.id].append(task)
    
    def _assetAvailabilityFilled(self, dateRange, asset):
        for assetIdParent in self._schedule.keys(): #Loop scheduled assets
            if assetIdParent <> asset.id: #Ignore if the asset is the one being scheduled on
                for taskParent in self._schedule[assetIdParent]: #Loop asset tasks
                    if taskParent.dateRange in dateRange: #If tasks overlap
                        usedAssets = [assetIdParent] #Add/Reset used asset
                        if len(usedAssets) >= self.maxAssetsInWork: return True #If assets filled, return
                        for assetIdChild in self._schedule.keys(): #Find other assets
                            if assetIdChild <> asset.id and assetIdChild <> assetIdParent: #Ignore same & scheduled assets
                                for taskChild in self._schedule[assetIdChild]: #Get asset tasks
                                    if taskChild.dateRange in taskParent.dateRange: #If task overlap
                                        usedAssets.append(assetIdChild) #Add used asset
                                        if len(usedAssets) >= self.maxAssetsInWork: return True #If assets filled, return
                                        break #Stop looking at tasks for this child asset
        return False
    
    def _skillAvailabilityFilled(self, task):
        for skill in task.skills: #Loop task skills
            for assetIdParent in self._schedule.keys(): #Loop scheduled assets
                for taskParent in self._schedule[assetIdParent]: #Loop asset tasks
                    if taskParent.dateRange in task.dateRange: #Select overlapping tasks
                        for skillParent in taskParent.skills: #Loop skills
                            if skillParent.id == skill.id: #If same skill
                                usedSkills = skill.total + skillParent.total #Add/Reset used skills
                                if usedSkills > skill.available: return True #If no room, return
                                for assetIdChild in self._schedule.keys(): #Find other assets
                                    for taskChild in self._schedule[assetIdChild]: #Get asset tasks
                                        if taskChild.dateRange in taskParent.dateRange: #If task overlap
                                            if assetIdChild <> assetIdParent or taskParent.id <> taskChild.id: #If not same asset task
                                                for skillChild in taskChild.skills: #Loop skills
                                                    if skillChild.id == skillParent.id: #If same skill
                                                        usedSkills += skillChild.total #Add used skills
                                                        if usedSkills > skill.available: return True #If no room, return
        return False
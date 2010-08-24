class PushToRight:
    def __init__(self, input):

        from datetime import timedelta
        
        #for task in input.tasks:
        #    print task.resourcePercent, task.id
        
        
        #sorted(input.tasks, key=lambda task: task.relativeWeight)

        #for task in input.tasks:
        #    print task.resourcePercent, task.id

        conflicts = 0
        
        for asset in input.assets:
        
            for task in input.tasks:
                
                if(task.interval):
                
                    start = task.next(asset, input.schedule.last(asset, task))
                    
                    while(start <= task.dateRange.end):
                        
                        while(input.schedule.blocked(asset, task, start)): 
                        
                            start += timedelta(days=1) #Shift to the right one day when blocked
                            
                            conflicts += 1
                            
                        end = input.schedule.add(asset, task, start)
                    
                        #print asset.name, task.name, start, end
                        
                        start = task.next(asset, end)
                    
        print "PushToRight", input.schedule.dataSource, "Manhours:", input.schedule.totalManhours, " Shifts:", conflicts
                    
                #TODO: 
                #No Maintenance Period
                #planned usage
                #task start/end dates
                #number per a year FY
                #configuration
                #pre tasks (any occurrence before self)
                #order tasks by largest size / availability
class PushToRight:
    def __init__(self, input):

        from datetime import timedelta
        
        input.tasks.sort(key=lambda task: task.relativeWeight)
        
        conflicts = 0
        
        for asset in input.assets:
        
            for task in input.tasks:
                
                start = task.next(asset, input.schedule.last(asset, task))
                
                while(start <= input.schedule.dateRange.end):
                    
                    while(input.schedule.blocked(asset, task, start)): 
                    
                        start += timedelta(days=1) #Shift to the right one day when blocked
                        
                        conflicts += 1
                        
                    end = input.schedule.add(asset, task, start)
                
                    #print asset.name, task.name, start, end
                    
                    start = task.next(asset, end)
                    
        print "PushToRight", input.schedule.dataSource, "Manhours:", input.schedule.totalManhours, " Counts:", conflicts
                    
                #TODO: 
                #No Maintenance Period
                #planned usage
                #task start/end dates
                #number per a year FY
                #configuration
                #pre/post/conflicting tasks
                #pre tasks
                #schedule precision
                #order tasks by largest size / availability
from random import shuffle

workgroups = ['CM','Database','Engineering','Process','Testing','Training','Usability','Security']
positions = ['1','2','3']

team = ['Cameron','Carl','Chris','Jeff','Jim','John M','John S','Nick','Rich','Scott','Steve','Tim']
devs = []

for position in positions:
    for workgroup in workgroups:
        if not len(devs): 
            devs = team[:]
            shuffle(devs)
        print workgroup, '\t', position, '\t', devs.pop()
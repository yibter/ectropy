from datetime import date
from datetime import timedelta
from random import randint
from inputs.iSUMOe6Random import iSUMOe6Random

d = iSUMOe6Random()

source = open('inputs/iSUMOe6Random.py', 'r')
f = open('iSUMOe6Random.py', 'w')

line = source.readline()
 
while line:
    if line.strip().startswith('self.assets'): break
    if not line.strip().startswith('schedule.force'): f.write(line)
    line = source.readline()

for t in d.tasks:
    if t.interval:
        for a in d.assets:
            schedule = date.today() - timedelta(days=randint(0,t.interval)) #random date
            schedule = "datetime("+str(schedule.year)+", "+str(schedule.month)+", "+str(schedule.day)+")"
            f.write("\t\tschedule.force(assets["+str(a.id)+"], tasks["+str(t.id)+"], DateRange("+schedule+", "+schedule+"))\n")

while line:
    f.write(line)
    line = source.readline()

source.close()
f.close()

print "done"
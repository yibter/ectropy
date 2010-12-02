from random import randint, choice
from inputs.iSUMOe6Random import iSUMOe6Random

d = iSUMOe6Random()
assetIds = [x.id for x in d.assets]
taskIds = [x.id for x in d.tasks]

initial_total_min = 10
initial_total_max = 20
initial_year_min = 1998
initial_year_max = 2009
initial_month_min = 1
initial_month_max = 12
initial_day_min = 1
initial_day_max = 27

source = open('inputs/iSUMOe6Random.py', 'r')
f = open('iSUMOe6Random.py', 'w')


line = source.readline()
 
while line:
    if line.strip().startswith('self.assets'): break
    if not line.strip().startswith('schedule.force'): f.write(line)
    line = source.readline()


for x in range(randint(initial_total_min, initial_total_max)):
    schedule = "datetime("+str(randint(initial_year_min,initial_year_max))+", "+str(randint(initial_month_min,initial_month_max))+", "+str(randint(initial_day_min,initial_day_max))+")"
    f.write("\t\tschedule.force(assets["+str(choice(assetIds))+"], tasks["+str(choice(taskIds))+"], DateRange("+schedule+", "+schedule+"))\n")

while line:
    f.write(line)
    line = source.readline()

source.close()
f.close()

print "done"
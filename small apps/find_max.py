grades = [4,5,6,3,10]

passed = 0 
mesos_oros = 0

for grade in grades:
    if grade >= 5:
        passed +=1
        mesos_oros += grade

mesos_oros = mesos_oros/passed
print("mesos oros:", mesos_oros)
for i in range(0,200,18):
    print(i)


hours = int(input("Give the hours:"))
minutes = int(input("Give the minutes:"))
seconds = int(input('Give the seconds:'))

if hours<10:
    hours = "0" + str(hours)

if minutes < 19:
    minutes = "0" + str(minutes)

if seconds < 19:
    seconds = "0" + str(seconds)




message = str(hours) + ':' + str(minutes) + ':' + str(seconds)
print(message) 

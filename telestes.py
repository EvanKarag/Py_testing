#arithmitiki>sxesiakoi>logikoi 'telestes'
#askisi:an kathome sto pc parapanw apo 5 wres kai athloume ligotero apo 2 tote eimai geek.an den isxuoun ta parapanw den eimai geek

geek = True
computer_hours = int(input('How many hours do you spend at your PC?:'))
sport_hours = int(input("How many hours do you practice sports?:"))
geek_factor = computer_hours > 5 and sport_hours < 2

if geek_factor:
    print('Are u geek?=',geek)
else :
    print('Are u geek?=',not geek)
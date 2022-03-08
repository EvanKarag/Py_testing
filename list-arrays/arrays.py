numbers = [1,3,1312,4]
team = ['zan','claud','van','dame']



#getin a value
for i in team:
    print(i)

#print length
print(len(team),len(numbers))

#adding
team.append('lisgevator')


#remove 
team.remove('lisgevator')

#insertin in pos
team.insert(2,'lisge')

#remove me pop
team.pop(1)

#reverse the list
team.reverse()

#sort alphabetical
team.sort()

#reverse sort
team.sort(reverse=True)
print(team)

#tuple=stixio pou den allazei me tipota,//ena stixio to kanei lista STRING xoris , sto telos

team2 = tuple('lisge')
print('team2',team2)

#delete tuple
del team2


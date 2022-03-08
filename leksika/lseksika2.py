string = "Dictionaries are collections of key, value pairs. Printing a dictionary displays all key, value pairs stored in the dictionary.jsasjdhfskdjhfaksdjfhsd"

my_list = list(string)
print(my_list)

dictionary = {}

for char in my_list:
    if char not in dictionary:
        dictionary[char] = 1
    else:
        dictionary[char] += 1

max_value = max(list(dictionary.values()))

for key,value in dictionary.items():
    if value == max_value:
        print("This is the max value:",key)
    

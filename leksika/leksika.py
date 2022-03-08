dictionary = {
    "ιταμος" : "προκλητικος, αυθαδης,αναιδης",
    "ονειδος" : "ντροπη,καταισχυνη",
    " πομφολυγες" : " αερολογιες,σαχλαμαρες"
}

print(dictionary)

dictionary[ "flhnamfimata"] = "anoisies,saxlamares"

key = input(" Δωσε λεξη για το λεξικο :")
value = input("δωσε επεξηγηση:")

dictionary[key] = value
print(dictionary)

person = {
    "name": "evangelos",
    "surname": "karajohn",
    "birth_date": "16/1/97",
    "address": "bando",
    "phone": "6918713126"
}

print("Name:"+person["name"]+ "\n" + "Eponumo:"+ person[ "surname"] + "\n"+ "DOB:"+ person["birth_date"]+ "\n"+ "Address:" + person["address"]+ "\n"+ "Phone:" + person["phone"])


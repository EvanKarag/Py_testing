number = int(input("Give one number for the list:"))
boole = True 
lista = []
wana_continue = 1

while boole:
    wana_continue = int(input("Wana continue giving numbers?Press 1 for yes,2 for no:"))
    while (wana_continue !=1) and (wana_continue != 2):
        wana_continue = int(input("Wana continue giving numbers?Press 1 for yes,2 for no:"))
        
    if wana_continue == 2:
        boole = False 
    else:
        number = int(input("Give one number for the list:"))
        lista.append(number)
        lista.sort()
        print(lista)

    
    
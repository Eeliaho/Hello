import random
salaisuus = random. randint(1, 10)
print("arvaa luku väliltä 1-10")
while True:
    arvaus = int(input("anna arvaus: "))
    if arvaus > salaisuus:
        print("liian suuri arvaus")
    elif arvaus < salaisuus:
        print("liian pieni arvaus")
    else:
        print("oikein, luku on", salaisuus)
        break

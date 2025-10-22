import random

luku = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for i in range(luku):
    heitto = random.randint(1, 6)
    print("arpakuutio", i+1,heitto)
    summa += heitto

print("Silmälukujen summa on",summa)

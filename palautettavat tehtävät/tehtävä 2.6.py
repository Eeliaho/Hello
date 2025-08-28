import random
kolmenumerokoodi = ""
for i in range(3):
    kolmenumerokoodi += str(random.randint(0, 9))

print("Kolmenumeroinen koodi:", kolmenumerokoodi)

nelinumerokoodi = ""
for i in range(4):
    nelinumerokoodi += str(random.randint(1, 6))

print("nelinumerokoodi:", nelinumerokoodi)


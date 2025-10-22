luvut = []

while True:
    luku = (input("anna luku tai lopeta painamalla enter: "))
    if luku =="":
        break
    luvut.append(luku)
luvut.sort(reverse=True)
for luku in luvut[:5]:
    print(luku)


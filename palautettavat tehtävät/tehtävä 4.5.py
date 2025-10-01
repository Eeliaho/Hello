käyttäjätunnus = "python"
salasana = "rules"
yritykset = 0
maks_yritykset = 5
while yritykset < maks_yritykset:
    tunnus = input("anna käyttäjätunnus: ")
    salasana = input("anna salasana: ")
    if tunnus == "python" and salasana == "rules":
        print("tervetuloa")
        break
    else:
        print("väärä tunnus tai salasana")
        yritykset += 1
if yritykset == maks_yritykset:
    print("pääsy evätty")



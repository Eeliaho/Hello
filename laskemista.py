pituus = int(input("anna pituutesi: "))
paino = float(input("anna painosi: "))

#muuttuja jossa lasku suori
bmi = paino / (pituus / 100) ** 2
print("pituus-paino-indeksisi on",bmi)
print(f"pituus-paino-indeksisi on {bmi:10.2f}")


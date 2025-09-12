sukupuoli = input("kerro sukupuolesi (nainen/mies): ").lower()
gl = int(input("kerro hemoglopiini arvosi: "))
if sukupuoli == "mies":
    if gl < 134:
        print("hemoglopiinisi on alhainen")
    elif gl > 195:
        print("hemoglopiinisi on korkea")
    elif 134 <= gl <= 195:
        print("hemoglopiinisi on normaali")
if sukupuoli == "nainen":
    if gl < 117:
        print("hemoglopiinisi on alhainen")
    elif gl > 175:
        print("hemoglopiinisi on korkea")
    elif 117 <= gl <= 175:
        print("hemoglopiinisi on normaali")




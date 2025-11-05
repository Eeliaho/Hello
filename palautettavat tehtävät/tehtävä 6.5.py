def parilliset(luvut):
    return [luku for luku in luvut if luku % 2 == 0]

def main():
    numerot = [1,4,6,8,3,11,13]

    pariluvut = parilliset(numerot)

    print("alkuperäinen lista on: ", numerot)
    print("listan parilliset luvut ovat: ", pariluvut)
if __name__ == "__main__":
    main()


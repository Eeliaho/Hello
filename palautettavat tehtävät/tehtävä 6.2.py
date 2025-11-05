import random
def heitänoppaa(tahkojenmäärä):
    return random.randint(1, tahkojenmäärä)
def main():
    tahkojenmäärä = int(input("anna tahkojen määrä: "))

    silmäluku = 0
    while silmäluku != tahkojenmäärä:
        silmäluku = heitänoppaa(tahkojenmäärä)
        print("heiton tulos", silmäluku)
if __name__ == "__main__":
    main()

def muunnos(gallonat):
    return gallonat * 3.785

def main():
    while True:
        gallonat = float(input("anna polttoaineen määeä galloonoina, negatiivinen lopettaa: "))
        if gallonat < 0:
            break

        litrat = muunnos(gallonat)
        print("gallonnaa on litroina", litrat)
if __name__ == "__main__":
    main()
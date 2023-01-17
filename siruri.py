def inlocuire():
    sir = input()
    sirnou = ""
    for caracter in sir:
        if caracter in "aeiou":
            sirnou += caracter.upper() #sirnou = sirnou + caracter.upper
            print(caracter.upper())
        else:
            sirnou += caracter #sirnou = sirnou + caracter
            print(caracter)
    print(sirnou)


def schimbarecuvant():
    cuvant = input()
    index = 0
    cuvantnou = ""
    for caracter in cuvant:
        if index == 0:
            cuvantnou += caracter.upper()
            print(caracter.upper(), "am gasit primul element", index)
        else:
            if index == len(cuvant)-1:
                cuvantnou += caracter.upper()
                print(caracter.upper(), "am gasit ultimul element", index)
            else:
                cuvantnou += caracter
                print(caracter, index)
        index += 1
    print(cuvantnou)


def halsort():
    lista = [34, 0, 2, 5, 3, 300, 56]
    jumatate = len(lista) // 2
    print


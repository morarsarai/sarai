# de realizat o functie care verifica intr-un sir numarul de aparitii a cifrei 5
def sir5():
    print('Va rog introduceti un sir de numere naturale')
    sir = input()
    print(sir)
    contor = 0
    for index in range(0,len(sir)):
        if int(sir[index]) == 5:
            contor += 1
    print('contor=', contor)


def lista5():
    print('Va rog introduceti un sir de numere naturale despartite prin spatiu:')
    lista = input().split("")
    contor = 0
    for index in range(0, len(lista)):
        if int(lista[index]) == 5:
            contor += 1
    print("contor=", contor)


# de realizat o functie care preia un numar de la tastatura si incadreaza acel numar in domeniile urmatoare
# 0 -> 3500 - mic
# 3500 -> 7000 - mediu
# 7000 -> - mare
def incadrare():
    print('Introduceti un numar:', end="")
    o = int(input())
    if o < 3500:
        print("mic")
    else:
        if o < 7000:
            print("mediu")
        else:
            print("mare")


# de realizat un meniu simplu, de genul
# Apasati tasta 1 pentru adunare, 2 pentru scadere, 3 pentru inmultire, 4 pentru impartire
def adunare():
    print('a=', end='')
    a = int(input())
    print('b=', end='')
    b = int(input())
    print('a+b=', a-b)


def scadere():
    print('a=', end='')
    a = int(input())
    print('b=', end='')
    b = int(input())
    print('a-b=', a - b)


if __name__ == "__main__":
    scadere()
sm = 0

def adunarecametoda(*args):
    global sm
    for a in args:
        sm += a

def adunare(*a):
    s = 0
    for element in a:
        s = s + element
    return s


def adunare2lista(lista):
    listanoua = list()
    for i in range(len(lista)):
        listanoua.append(lista[i]+2)
    return listanoua


def inmultire2lista(lista):
    listanoua = list()
    for i in range(len(lista)):
        listanoua.append(lista[i]*2)
    return listanoua


def oglindit(n):
    return int(str(n)[::-1])

# primul parametru este o lista de numere intregi
# al doilea parametru reprezinta valoare initiala a sumei finale si rezultatul functiei sale

def adunarelista(lista, s=0):
    # aici execut o parcurgere a listei de intrare si ...
    for i in range(len(lista)):
        s += lista[i]
    return s


# verificare numar prim
def verificarePrime():
    # daca numarul este 2 atunci un numar prim prin
    if numar == 2:
        return True
    #daca este mai mic ca si 2 atunci nu este prim
    if numar < 2:
        return False
    # daca numarul se imparte exact la 2 atunci nu este prim
    if numar % 2 == 0:
        return False
    # luam numerele de la 3 pana la valoare numar impartit la 2
    for divizor in range(3, numar // 2):
        # daca numarul se imparte la divizor atunci nu e prim
        if numar % divizor == 0:
            return False
    # daca s-a ajuns aici insesamna ca numarul meu este prim
    return True


#gasire primului numar prim mai mare ca si n
def nr_prim(numar):
    # am nevoie de o variabila care sa imi spuna ca am gsit numarul prim
    # initializez variabila respectiva cu false sau 0
    gasit = 0
    # cat timp nu am gasit numarul
    while gasit == 0:
        # maresc numarul meu cu 1 si verific daca este prim
        numar = numar + 1
        # daca este prim modific variabila gasit in true, prin urmare while-ul se va opri
        if verificarePrime(numar):
            gasit = 1
    # reintor numarul gasit
    return numar


# opt poate lua valorile 1, 2 sau 3, unde 1 - adunare, 2 scadere iar 3 produs
def maniu3(opt): # specificam tipul parametrului/lor si ce reprezinta fiecare parametru
    if opt == 1:
        return "adunare"
    elif opt == 2:
        return "scadere"
    elif opt == 3:
        return "inmultire"
    else:
        return "operatie nedefinita"


def cifrezero():
    # am convertit numarul meu in sir de caractere
    sir = str(n)
    # am initializat un contor cu zero
    contor = 0
    # pentru fiecare caracter in sirul meu
    for caracter in sir:
        # verific daca este 0, iar daca da atunci incrementez contorul
        if caracter == "0":
            contor += 1
    # intorc ca si rezultat al functiei contorul definit de mine
    return contor


# produsul unor numere primite ca parametru de o functie
def produsul(*args):
    p = 1
    for a in args:
        p = p * a
    return p


# factorialul unui numar n, n!
def factorial():
    f = 1
    i = 1
    # varianta cu while
    while i<=n:
        f = f * i
        i = i+1
        # varianta cu for
    for i in range(1,n+1):
        f = f*i
    return f


if __name__ == "__main__":
    # v1 = adunare(1,2,3,4,5,6)
    # v2 = adunare(3)
    # v3 = adunare()
    # print(v3)
    # print(adunare(v1,v2,v3))
    adunarecametoda(1,2,4,5)
    print(sm)
    print(adunare(1,2,4,5))
    print(adunare2lista([1,2,3,4]))
    print(inmultire2lista([1,2,3,4]))
    print(oglindit(123456))
    s1 = 10
    print(adunarelista([1,2,3,4], s1))
    print(cifrezero(1200023000))
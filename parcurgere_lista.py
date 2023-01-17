def lista():
    l1 = list()
    l1 = [1, 2, 3, 4, 5, 6, 7]
    for element in l1:
        print(element)
    for i in range(len(l1)):
        print(l1[i])

# am cuvantul abc iar a are valoarea 10, b 20, c 30 -> 10+20+30
# {a:10, b:20, c:30, ... }

def lista_abc():
    l1 = list()
    a = 10
    b = 20
    c = 30
    l1 = [a+b+c]
    for element in l1:
        print(element)
    for i in range(len(l1)):
        print(l1[i])

def suma_litere():
    # definesc dictionarul / hash table
    # sub forma de mai jos
    dic1 = {'a':10, "b":20, "c":30}
    suma = 0
    cu = "abc"
    for i in range(len(cu)):
        suma+= dic1[cu[i]]
    print("Suma este:", suma)


def crypt_hash(propozitie):
    dict3crypt = {"a":"d","b":"e","c":"f","d":"g","e":"h","f":"i","g":"j",
                  "h":"k","i":"l","j":"m","k":"n","l":"o","m":"p","n":"q",
                  "o":"r","p":"s","q":"t","r":"u","s":"v","t":"w","u":"x",
                  "v":"y","w":"z","x":"a","y":"b","z":"c"}
    rezultat = ''
    for element in propozitie:
        if element in ('',',','-','?','1','2','3','4','5','6','7','8','9','0'):
           rezultat += element
        else:
            rezultat += dict3crypt[element]
    return rezultat

def decrypt_hash(propozitie):
    dict3crypt = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j",
                  "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q",
                  "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x",
                  "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}
    rezultat = ''
    for element in propozitie:
        if element in ('',',','-','?','1','2','3','4','5','6','7','8','9','0'):
            rezultat += element
        else:
            rezultat += dict3crypt[element]
    return rezultat




if __name__ == "__main__":
    propozitie = input()

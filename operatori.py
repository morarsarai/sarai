def sumanumere():
    print("Introduceti primul numar, a")
    a = input()
    print("Numarul introdus a=", a)
    print("Introduceti al 2-lea numar, b")
    b = input()
    print("Numarul introdus b=", b)
    print("a+b =", int(a)+int(b))

def scaderenumere():
    print("Introduceti primul numar, a")
    a = input()
    print("Numarul introdus a=", a)
    print("Introduceti al 2-lea numar, b")
    b = input()
    print("Numarul introdus b=", b)
    print("a-b =", int(a) - int(b))


def inmultirenumere():
    print("Introduceti primul numar, a")
    a = input()
    print("Numarul introdus a=", a)
    print("Introduceti al 2-lea numar, b")
    b = input()
    print("Numarul introdus b=", b)
    print("a*b =", int(a) * int(b))


def impartirenumere():
    print("Introduceti primul numar, a")
    a = input()
    print("Numarul introdus a=", a)
    print("Introduceti al 2-lea numar, b")
    b = input()
    print("Numarul introdus b=", b)
    print("a/b =", int(a) / int(b))


def arietriunghidr():
    print("Introduceti primua cateta, ab")
    ab = input()
    print("ab=", ab)
    print("Introduceti a 2-a cateta, ac")
    ac = input()
    print("ac=", ac)
    print("(ab*ac)/2=", (int(ab)*int(ac))/2)


def perimetrul():
    print("Introduceti prima latura, ab")
    ab = input()
    print("ab=", ab)
    print("Introduceti a 2-a latura, bc")
    bc = input()
    print("bc=", bc)
    print("Introduceti a 3-a latura, ac")
    ac = input()
    print("ac=", ac)
    print("ab+bc+ac=", (int(ab)+int(bc)+int(ac)))


if __name__ == "__main__":
    sumanumere()
    scaderenumere()
    inmultirenumere()
    impartirenumere()
    arietriunghidr()
    perimetrul()
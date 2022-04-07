from math import sqrt

print("1. Afișați în consolă rezultatul expresiei: 9 * (12-5) - 2**3")
print(9 * (12-5) - 2**3)

print("\n2. Realizați un nou program care calculează și afișează șapte la puterea a treia.")
print(7**3)
a = 7
p = 1
for i in range(3):
    p = p * a
print("{} este 7 la puterea a 3-a".format(p))

def nr_putere(aa):
    p = 1
    for i in range(3):
        p = p * aa
    print("{} este {} la puterea a 3-a".format(p,aa))

nr_putere(2)
nr_putere(8)
nr_putere(3)

print("\n3. O mașină folosește o cantitate de x litri. O altă mașină folosește y=2*x litri. Să se scrie un program în care să se citească variabila x și să se determine suma necesarului de combustibil.")
def litri():
    x = int(input("Litri prima masina: "))
    print(f'Litri {2*x} a doua masina')
    print('Litri {} total'.format(x+2*x))
litri()

print(int("110"))

print("\n5. Creați un convertor de timp, transformând astfel orele și minutele introduse de la tastatură în secunde.")
def secunde(ore, min):
    total_secunde = ore * 3600 + min * 60
    print(total_secunde)
secunde(5,54)
secunde(7,32)

print("\n6. Se citesc patru numere întregi. Afișați media geometrică și media aritmetică a acestora.")
def media(a,b,c,d):
    ma = (a+b+c+d)/4
    mg = sqrt(a*b*c*d)
    print(f'Media aritmetica a numerelor {a}, {b}, {c}, {d} este: {ma} \nMedia geometrica a numerelor {a}, {b}, {c}, {d} este: {mg}')
media(2,8,10,22)

print("\n7. Citim de la tastatură un număr natural n. Puteți afișa răsturnatul lui?")
def invers_nr(n):
    inv = ''
    for i in range(len(n), 0, -1):
        inv += n[i - 1]
    print(f'Inversul lui {n} este :', inv)
invers_nr('12345')

print("\n8. Fie x un număr natural de exact 4 cifre. Să se calculeze produsul cifrelor sale.")
def prod_cifre(nr):
    p = 1
    while nr > 1:
        r = nr % 10
        nr = nr // 10
        p = p * r
    print(p)

prod_cifre(2143)

print("\n9. Se citesc trei valori reale a, b, c. Să se precizeze dacă ele pot fi laturile unui triunghi.")
def laturi_triunghi(a, b, c):
    if a + b >= c and a + c >= b and b + c >= a:
        print("Avem triunghi!")
    else:
        print("Nu avem Triunghi!")
laturi_triunghi(11, 22, 33)
laturi_triunghi(15, 15, 15)
laturi_triunghi(5, 3, 9)

print("\n10. Tipăriţi toate numerele prime aflate între două numere naturale citite.")
def nr_prime(a, b):
    for nr in range(a, b + 1, 1):
        if nr > 1:
            for j in range(2,nr):
                if nr % j == 0:
                   break
            else:
                print(i)
nr_prime(0,98)

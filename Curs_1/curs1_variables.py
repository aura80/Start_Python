#variables
"""" In this page will make exercise with variables """
car = "Dacia"
_car = "Mazda"
number_of_cars = 4
numberOfCars = 4
PI = 3.14
URL = "www.emag.ro"
print("Hello")
print(PI)
a = 5
b = 3
print(a+b)
print("suma este ", a+b)
print("catul este ", a/b)
print("modulus este ", a%b)
print("Adunarea este", 5+6)
print("Adunarea este "+ "IMPORTANTA " + "5", 2+1)
#integer
aa = 5
#float
bb = 4.5
#string
nume = "Ioana"
nume = 'Vasile'
#boolean
isCorrect = True
print(aa+bb)
aa = aa+1       # incrementare
aa += 4        # incrementare
print(aa+bb)
print(aa)
print(nume)
print(type(isCorrect))
print(type(nume))
print(type(b))

adresa = "strada somesului"
print("adresa mea este", {adresa})
print(f'adresa mea este {adresa}')
print(f'numele meu este ioana')
print(f'numele meu este {nume}')
print('salut numele meu e {}'.format(nume))

# string
fraza = "Ana are mere"
print("lungirea sirului", len(fraza))
print("prima pozitie", fraza[0])
print("ultima pozitie", fraza[11])
print("out of range", fraza[3])
print("substring", fraza[3:5])
print("substring", fraza[3:7])  #substring
print("substring numere pozitie para", fraza[::2])
print(fraza[-2])
print("substring afisare inversa:", fraza[::-1])

nume = "alex"
print(nume.upper())
print(nume.capitalize())
fraza = fraza.replace("ioana", "ana")
print(fraza.replace("ana", "ioana"))
print(fraza.find("a"))
print(nume.find("l"))

curs = input("citeste un numar")
print(curs)
year_birth = input("citeste un numar")
an = 2021
print(an-int(year_birth))

a = input("primul numar este")
b = input("al doilea numar este")
print("suma este", int(a)+int(b))

c = int(input("c primul numar este"))
d = int(input("d al doilea numar este"))
print("produsul este", c*d)

# a = {"ana","are","mere"}  #lista

assert a == b

#   == #egal
#   != #not egal
#   in #cauta daca un string e in alt string

assert   int(a) > 18 and int(a) < 55
# assert   a > 18 or a < 55
assert "in" in "alina3"


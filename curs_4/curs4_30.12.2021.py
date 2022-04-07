a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
d = int(input("d= "))

if c + d > 0:
    print("a + b = ", a+b)
elif c + d == 0:
    print("a - b = ", a-b)
else:
    print("a * b = ", a * b)

zi = int(input("Dati un numar: "))
if zi == 1:
    print("Azi e luni")
elif zi == 2:
    print("Azi e marti")
elif zi == 3:
    print("Azi e miercuri")
elif zi == 4:
    print("Azi e joi")
elif zi == 5:
    print("Azi e vineri")
elif zi == 6:
    print("Azi e sambata")
else :
    print("Azi e duminica")

print("Dana, Maria")
w = input()
l = ["Dana", "Maria"]
for w in l:
    if l[0] < l[1]:
        print(l[1])
    else:
        print(l[0])

t = str(input("*****     Doua cuvinte: ")).split()
if (len(t[0]) > len(t[1])):
    print("     the longest has " + str(len(t[0])) + " letters and the word is " + "'" + t[0] + "'")
else:
    print("          Mai lung este " + "'" + t[1] + "'")

tt = str(input("*****     Trei cuvinte: ")).split()
if ((len(tt[0]) > len(tt[1])) and (len(tt[1]) > len(tt[2]))):
        max = len(tt[0])
        maxim = tt[0]
        print(" {} litere are cuvantul mai mare - ".format(max), maxim)
elif (len(tt[0]) > len(tt[1]) and len(tt[1]) < len(tt[2])):
    if len(tt[0]) > len(tt[2]):
        max = len(tt[0])
        maxim = tt[0]
        print(" {} litere are cuvantul mai mare - ".format(max), maxim)
    elif len(tt[0]) < len(tt[2]):
        max = len(tt[2])
        maxim = tt[2]
        print(" {} litere are cuvantul mai mare - ".format(max), maxim)
elif (len(tt[0]) < len(tt[1]) and len(tt[1]) < len(tt[2])):
    max = len(tt[2])
    maxim = tt[2]
    print(" {} litere are cuvantul mai mare - ".format(max), maxim)
elif (len(tt[0]) < len(tt[1]) and len(tt[1]) > len(tt[2])):
    max = len(tt[1])
    maxim = tt[1]
    print(" {} litere are cuvantul mai mare - ".format(max), maxim)

text = input("Scrie un cuvant: ")
t_1 = text[::-1]
print("Scrise in sens invers: \n" + t_1)
print("\nLower: " + t_1.lower() + "\nUpper: " + t_1.upper())
print("Cu litera mare la inceput: ", t_1.capitalize())

def cuvinte(a, b):
    print("Noul cuvant: " + a[-1] + b[0:2])
    print("Noul cuvant: " + a[len(a)-1] + b[0:2])

cuvinte("Ana", "are")

#Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the o
#of a specified string. If the length of the string is less than 3 then return the original string
def f(sir):
    if len(sir) < 3:
        return sir
    else:
        return(sir[0:3])
print(f("fydfgadshfb"))
print(f("abc"))
cuvinte(f("prajitura"),"maria")

list = ["ana", "vasile", 34, 55, 89, True, False, 45.6, ["ana", "are", "6", "mere"]]
lista = ["ana", "ioan", "george"]
print(list[0])
print(list[-1][1])
print(list[3:2])
print(list[2:2])
print(list[2:])
print(list[::-1])

nume = "ana"
nume_2 = nume
print(nume_2)

list_2 = list
print(list_2)
list.append("dfghjklugrhjkgfn")
print(list)
list.pop()
print(list)
lista.sort()
print(lista)
print(list[-1:1])

#suma elementelor listei /pare/ impare/ suma/ produs
def sum_of_list():
    list = [2,3,4,5,6,6,6,8,9]
    sum = 0
    for element in list:
        if (element%2 == 0):
            sum = sum + element
        else:
            impar = element
            print("Impare:", impar)
    print("Suma pare = ", sum)

sum_of_list()

prod = 1
for elem in range(1,6):
    prod *= elem
    print(prod)

prod = 1
for el in range(1,6):
    assert elem == 5
    print(el)
print(prod)

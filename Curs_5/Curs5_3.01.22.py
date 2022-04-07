print("\n15: Use a loop to display elements from a given list present at odd index positions produsul elemenetelor de pe pozitie para")
lista = [5, 10, 85, 30, 4, 6]
p = 1
pp = 1
for i in lista:
    if lista.index(i) % 2 == 0:
        p = p*i
print("Produs numere de pe index par: ", p)

for j in range(0,len(lista),2):
    pp = pp * lista[j]

print(p)

def adaugare_lista():
    l = []
    for i in range(1000,10,-2):
        print(i)
        l.append(i)
    print(l)
adaugare_lista()

print("\n16. Print n asterisks")
def print_asterisc(n):
    for i in range(n+1):
        i = "*"*i            # le ia de la 1 la n
    print("Stelute: ", i)
    for i in range(n):       # le ia de la 0 la n-1
        print("*")
print_asterisc(5)

print("\n17. Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)")

for i in range(1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        print("Numerele divizibile si cu 7 si cu 5 sunt: ", i)

print("\n18. Write a Python program to count the number of even and odd numbers from a series of numbers.")
#  Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
pare = 0
impare = 0
for i in numbers:
    if i % 2 == 0:
        print("pare: ", i)
        pare = pare + 1
    else:
        print("impare: ", i)
        impare += 1
print("Pare: ", pare)
print("Impare: ", impare)
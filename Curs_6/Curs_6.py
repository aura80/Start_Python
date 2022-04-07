list1 = [3, 5, 98, -5]
list2 = [0, 7, 5, 98, 876]
l = list1[:]
for i in l:
    if i in list2:
        list1.remove(i)
        list2.remove(i)
list1.extend(list2)
print(list1)

for i in list1:
    for j in list2:
        if i == j:
            list1.remove(i)
        list2.remove(j)

list1.extend(list2)
print(list1)

list1 = [3, 5, 98, -3]
list2 = [0, 7, 5, 98, 876]
copy_of_list1 = list1[:]
for i in copy_of_list1:
    if i in list2:
        list1.remove(i)
        list2.remove(i)
list1.extend(list2)
print(list1)


dict = {"name":"Plato", "country":"Ancient Greece", "born":"-427", "teacher":"Socrate", "Student":"Aristotel"}
print(dict)
print(dict.items())
dict.update({"curs":"tata"})
print(dict)
dict.update({"curs":"ion"})
print((dict))
print(dict.get("name"))
print(dict.values())
dict2 = {1:"ion", 2.4:"vasile", 3:5, "ionela":"mama", "list":[3,4,5,6], "dict45":{6:4, 5:6, "eu":"tu"}}
print(dict2)
dict3 = {"ianuarie":31, "februarie":[28,29]}
zodie = {"rac":["ianuarie", 10,23]}

dictt={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
print(dictt.values())
dictt.update({"son's height": 2})       # face update la lista
print("Lista updatata:\n", dictt)
print(dictt.get("son's height"))        # returneaza valoarea unei chei
dictt.pop("son's height")   # sterge ce-i dam sa stearga prin cheie
print(dictt)
dictt.popitem()     # sterge ultimul din lista
print(dictt)
dictt.clear()       # sterge tot din dictionar
print(dictt)

n = int(input("numarul este: "))
#cat timp e adevarat
i = 0
sum = 0
while i <= n:
    sum = sum  + i
    i = i + 1
print(sum)

i = 4
prod = 1
while i >= 1:
    prod = prod * i
    i = i - 1
print(prod)

list = ["Bucuresti", "3&_budaPesta", "PARIS", " "]
l = []
print(list)
#print(type(list[0]))
i=0
while i < len(list):

    if (list[i].isupper())==True:
        l.append(list[i])
        print("-", l)
        i += 1
    else:
         print("***")
         l.append(list[i].upper())
         i += 1
    # i += 1
print(l)

list = ["Bucuresti", "budaPesta", "Paris"]
l = []
print(list)
i=0
while i < len(list):

    if list[i].capitalize():
        l.append(list[i].upper())
        i += 1
    else:
        l.append(list[i].upper())
        i += 1
    # i += 1
print(l)

lista = ["ana", "Ana", "VASILE"]
i = 0
while i < len(lista):
    print(lista[i])

    if lista[i].isupper():      # verifica daca toate literele cuvantului sunt mari
        lista[i] = lista[i][1:]       # omite prima litera
    i += 1
print(lista)

j = 0

while j in range(5):
    if j%2 == 0:
        print(j)
    j += 1

for i in range(2):
    nr = 0
    suma = 0
    while nr >= 0:
        suma += nr
        nr = eval(input("Introduceti un numar pozitiv: "))

    print("Suma numerelor introduse este: ", suma)
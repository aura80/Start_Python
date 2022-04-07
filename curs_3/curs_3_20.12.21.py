def adunare():
    print("sum is ", 5 + 6)
adunare()

def adunare_param(a,b):
    print('sum is ', a + b)
adunare_param(5,6)
adunare_param(23,45)
adunare_param(23.5,34.6)

def is_number_prim(number):
    return True
print("numarul nostru: ", is_number_prim(10))

def day_of_week(today):
    if today  == "sambata" or today == "duminica" :
        print (" este weekend ")
    #elif:
    else:
        print("este doar " + today)

day_of_week("sambata")
day_of_week("luni")

def scadere (a, b):
    return a-b
print(scadere(12,5))

def print_details(nume, varsta, restanta):
    print(f'Hello {nume}, ai {varsta} ani, te rog plateste {restanta}')

print_details("ionut", "28", "56")

def print_details(nume, varsta, restanta = "0"):
    print(f'Hello {nume}, ai {varsta} ani, te rog plateste {restanta}')

print_details("ionut", "28")

def print_details(nume, restanta, varsta = "0"):
    print(f'Hello {nume}, ai {varsta} ani, te rog plateste {restanta}')

print_details("ionut", "56")


# print('sum is ', 5 + 6)
# print('sum is ', 6 + 10)
# print('sum is ', 23.5 + 34.6)
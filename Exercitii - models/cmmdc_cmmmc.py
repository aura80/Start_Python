m = int(input("m="))
n = int(input("n="))
#rețin valorile initiale
init_m = m
init_n = n
#calculez cmmdc
while m!=n:
    if m>n: m = m - n
    else: n = n - m
#m va reține cmmdc
print("cmmdc =",m)
#calculez cmmmc
cmmmc = init_m*init_n // m
print("cmmmc =",cmmmc)




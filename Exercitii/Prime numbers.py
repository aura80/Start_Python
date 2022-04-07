# generate prime numbers between a and b
# and b are not inclusive
a, b = [int(a) for a in input("Enter start and end of range (integer): ").split()]
psum = 0
for num in range(a + 1, b):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            psum = psum + num
        print(num, end=' ')

print("\nSum=", psum)


def prime(n):
    isprime = True
    if n < 2:
        isprime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                isprime = False
                break
    return isprime


a, b = map(int, input("Enter two integers: ").split())
print(a, b)
lst = [i for i in range(a, b + 1) if prime(i)]
print('Prime numbers between =', lst)
print('Sum = ', sum(lst))

def prime(a,b):
	for i in range((b-a)+1):
		for i in range(2,a):
			if a % i==0:
				a+=1
				break
		else:
			print(a)
			a+=1
prime(3,11)


def prime(n):
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            return (0)
    return (1)


a = int(input("Enter a:"))
b = int(input("Enter b:"))
result = []
for i in range(a, b + 1):
    if (prime(i)):
        result.append(i)
print(result)
print(sum(result))


list_Of_Prime = list()

def isPrime(num):
    flag = 0
    if num == 2:
        return 1
    elif num == 1:
        return 0
    else:
        for x in range(2, num):
            if (num % x) == 0:
                flag = 1
    if flag == 0:
        return 1


start = int(input("Enter your starting number: "))
end = int(input("Enter your ending number: "))
for x in range(start, end):
    if (isPrime(x) == 1):
        list_Of_Prime.append(x)
print(list_Of_Prime)
print(sum(list_Of_Prime))


n = int(input("Enter a number: "))
isPrime = True
if n > 1:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            isPrime = False
            break
    if isPrime:
        print("Prime")
    else:
        print("Not prime")
else:
    print("Not prime")

import random  # import random module

n = int(input("Enter a number: "))


# binpower is use to calculate binary exponentiation as discussed above.
def binPower(a, b, n):
    if b == 0:
        return 1
    if b % 2 == 0:
        return binPower(a * a % n, b // 2, n)
    else:
        return a * binPower(a * a % n, b // 2, n) % n


def probablyPrimeFermat(n, iter=5):
    if n < 4:
        return n == 2 or n == 3
    for i in range(iter):
        a = 2 + random.randint(0, n - 3)
        if binPower(a, n - 1, n) != 1:
            return False
    return True


if probablyPrimeFermat(n, iter=5):
    print("Prime")
else:
    print("Not Prime")

import random  # import random module

n = int(input("Enter a number: "))


# binpower has already been discussed in the Fermat theorem used to calculate binary exponentiation.
def binpower(a, b, n):
    if b == 0:
        return 1
    if b % 2 == 0:
        return binpower(a * a % n, b // 2, n)
    else:
        return a * binpower(a * a % n, b // 2, n) % n


# check composite function is used to confirm whether a number is composite or not, which fermat failed to check.
def check_composite(n, a, d, s):
    x = binpower(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for r in range(1, s):
        x = binpower(x, 2, n)
        if x == n - 1:
            return False
    return True


def MillerRabin_PrimalityTesting(n, iter=5):
    if n < 4:
        return n == 2 or n == 3
    s = 0

    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for i in range(iter):
        a = 2 + random.randint(0, n - 3)
        if check_composite(n, a, d, s):
            return False
    return True


if MillerRabin_PrimalityTesting(n):
    print("Prime Number")
else:
    print("Not Prime Number")





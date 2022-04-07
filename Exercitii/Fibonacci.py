# Function for nth fibonacci
# number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
    a = 0
    b = 1

    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


# Driver Program
print(fibonacci(9))

# This code is contributed by Saket Modi
# Then corrected and improved by Himanshu Kanojiya


#Method 1 ( Use recursion ) :
# Function for nth Fibonacci number

def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# Driver Program

print(Fibonacci(10))

# This code is contributed by Saket Modi


#Method 2 ( Use Dynamic Programming ) :
# Function for nth fibonacci number - Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1

FibArray = [0, 1]


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib


# Driver Program

print(fibonacci(9))

# This code is contributed by Saket Modi


#Method 3 ( Use Dynamic Programming with Space Optimization) :
# Function for nth fibonacci number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


# Driver Program

print(fibonacci(9))

# This code is contributed by Saket Modi


#Method 4 ( Using Arrays ) :
# creating an array in the function to find the nth number in fibonacci series. [0, 1, 1, ...]

def fibonacci(n):
    if n <= 0:
        return "Incorrect Output"
    data = [0, 1]
    if n > 2:
        for i in range(2, n):
            data.append(data[i - 1] + data[i - 2])
    return data[n - 1]


# Driver Program

print(fibonacci(9))

# This Code is contributed by Prasun Parate (prasun_parate)


# To find the n-th Fibonacci Number using formula
from math import sqrt


# import square-root method from math library
def nthFib(n):
    res = (((1 + sqrt(5)) ** n) - ((1 - sqrt(5))) ** n) / (2 ** n * sqrt(5))
    # compute the n-th fibonacci number
    print(int(res), 'is', str(n) + 'th fibonacci number')
    # format and print the number


#Method 5 ( Using Direct Formula ) :
# driver code
nthFib(12)

# This code is contributed by Kush Mehta
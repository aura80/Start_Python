#args stands for arguments. If the parameter of a function is *args, it can take in any number of Positional Arguments. args is basically like a tuple and we can iterate over it using the in operator. Since it is a tuple, it is immutable.
#**kwargs is similar to *args. The only difference is that it accepts multiple keyword arguments. Hence the name “kwargs”.


def func(*nums):
    sum = 0
    for number in nums:
        sum += number
    return sum

print(func(10,20,30))
print(func(10,20))
print(func(10,20,40))


def func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')
    print("-x-x-x-x-x-x-x")

func(a = 10, b = 20)
func(c = 100)
func(d = 10, b = 10, a = 200)


def func(**dictionary):
    for key, value in dictionary.items():
        print(f'{key} : {value}')
    print("-x-x-x-x-x-x-x")

func(a = 10, b = 20)
func(c = 100)
func(d = 10, b = 10, a = 200)


#Correct Order
def func(num1, num2, *args, **kwargs):
    print(f'num1 : {num1}')
    print(f'num2 : {num2}')
    print(f' args : {args}')
    print(f' kwargs : {kwargs}')

func(1,2,3,4,5,6,parameter1 = 10,parameter2 = 20)



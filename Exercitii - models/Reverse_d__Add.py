studentNames = ["Hannah", "Imogen", "Lewis", "Peter"]
print(studentNames[::-1])

studentName = ["Hannah", "Imogen", "Lewis", "Peter"]
studentName.reverse()
print(studentName)

studentNames = ["Hannah", "Imogen", "Lewis", "Peter"]
for i in reversed(studentNames):
	print(i)

studentNames = ["Hannah", "Imogen", "Lewis", "Peter"]
print(list(reversed(studentNames)))

#How to add two lists element-wise in Python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = []			#initialize result list

for (item1, item2) in zip(list1, list2):
    sum_list.append(item1+item2)
print(sum_list)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

sum_list = [a + b for a, b in zip(list1, list2)]

print(sum_list)

#Write a Python program to add two objects if both objects are an integer type.
def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "Inputs must be integers!"
   return a + b
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))

# Slices:
#
# Slices are objects so they can be stored in variables. Some data structures allow for indexing and slicing such as lists, strings, and tuples.
# We can use integers to specify the upper and lower bound of the slice or use a slice object.
s = slice(4,8)
lst = [1, 3, 'w', '3', 'r', 11, 16]
text = 'w3resource'
tpl = (2,4,6,8,10,12,14)
print(lst[s])
print(text[s])
print(tpl[s])
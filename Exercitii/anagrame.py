#Python Program to Check if Two Strings are Anagram
#Method #1 : Using sorted() function

# function to check if two strings are
# anagram or not
def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

    # driver code


s1 = "listen"
s2 = "silent"
check(s1, s2)

#Method #2 : Using Counter() function
# Python3 program for the above approach
from collections import Counter


# function to check if two strings are
# anagram or not
def check(s1, s2):
    # implementing counter function ne arata de cate ori apare un caracter
    if (Counter(s1) == Counter(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


# driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)

#Method #3 : Using set() function
'''\
Python3 program for implementation of checking string is anagram or not
using set function.
'''


def check(s1, s2):
    # Asserting length of string
    assert len(s1) == len(s2), 'The strings are not of same length'

    # Implementation of set function
    if set(s1.lower()) == set(s2.lower()):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

    # one liner for above implementation
    # print('The strings are anagrams.') if set(s1.lower()) == set(s2.lower()) else print('The strings aren\'t anagrams.')


# Driver code
if __name__ == '__main__':
    word1, word2 = 'listen', 'silent'
    check(word1, word2)


word = sorted('rac')
alternatives = ['car', 'girl', 'tofu', 'rca']

for alt in alternatives:
    if word == sorted(alt):
        print(alt)
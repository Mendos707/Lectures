"""
Под каждым комментарием нужно написать одну функцию
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""
import math

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = []
def mult2(list):

    list2 = [i * 2 for i in list]
    return list2

list2 = mult2(list1)
print(list2)



# Write a function that takes a list of numbers
# And returns same list but numbers multiplied by 2
# input: list of numbers
# output: list of numbers multiplied by 2

print(mult2(list2))



# Write a function that takes a list of numbers
# And returns same list but numbers multiplied by 4
# USE PREVIOUS FUNCTION TO CREATE THIS ONE
# input: list of numbers
# output: list of numbers multiplied by 4


def pal():
    phrase = input('Insert word or phrase: ').lower()
    rev_phrase =  phrase[::-1].split()

    if phrase.split() == rev_phrase:
        print(True)
        bool = True
    else:
        print(False)
        bool = False
    print(rev_phrase)
    print(phrase)
    return bool

pal()

# Write a function that will check if users input is palindrome
# "Able was I ere I saw Elba" is a palindrome!!!
# input: nothing
# output: boolean



def squared():
    x2 = [i ** 2 for i in range(1,31)]
    print(x2)

squared()

# Write a function that prints a list of squared numbers from 1 to 30
# input: nothing
# output: nothing


def prod():
    x = input('Please, insert list of numbers: ')
    xlistmult = math.prod(float(i) for i in x.split())
    print(xlistmult)
    return xlistmult
prod()

# Write a function that multiplies all numbers in a list provided by user
# input: nothing
# output: float of multiplied numbers



'''
Написать программу которая:
	1. Высчитывает возраст из заданых данных (current_year - нынешний год, year_of_birth - год рождения)
	2. Найти недостающую часть кода (code_2)
		a. найдите остаток от x деленого на y
		b. полученый результ умножте на 13
		c. извлеките квадратный корень из полученного результата
		d. возьмите целую часть от результа
	3. Соединить код в отдельную переменную
	    пример:
	        475-12-967
	4. Вывести строку:
		пример:
			Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.
'''

# years
current_year = 2022
year_of_birth = 1988
code_1 = '354'
code_3 = 132
user_name = 'John'
user_surname = 'Smith'
x = 152
y = 132

####### First attempt #######


def work1():
    age = current_year - year_of_birth
    # print(age)
    return age


def work3():
    code = code_1 + '-' + str(work2()) + '-' + str(code_3)
    # print(code)
    return code


def work2():
    remainder = x % y
    # print(remainder)
    remainder = remainder * 13
    # print(remainder)
    remainder = remainder ** 0.5
    # print(remainder)
    remainder = round(remainder)
    # print(remainder)
    return remainder


def work4():
    print('Hello ' + user_name + ' ' + user_surname + '. You are ' +
          str(work1()) + ' years old. Your secret code is ' + str(work3()) + '.')



####### Optimised attempt #######


def opt():
    age = current_year - year_of_birth
    code = code_1 + '-' + str(round((x % y * 13)**0.5)) + '-' + str(code_3)
    print('Hello ' + user_name + ' ' + user_surname + '. You are ' +
          str(age) + ' years old. Your secret code is ' + str(code) + '.')


work4()
opt()

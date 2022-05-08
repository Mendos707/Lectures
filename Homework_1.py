
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
    return age


def work3():
    code = code_1 + '-' + str(work2()) + '-' + str(code_3)
    return code


def work2():
    remainder = x % y
    remainder = remainder * 13
    remainder = remainder ** 0.5
    remainder = round(remainder)
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

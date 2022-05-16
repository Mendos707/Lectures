
def menu():
        user_choice = input('Please choose:\n'
                            '1.Say hello\n'
                            '2.Hypotenuse\n'
                            '3.Triangle\n'
                            '4.Random_list\n'
                            '5.Tupple_merge\n'
                            '6.Most_popular\n'
                            '7.Seconds\n'
                            '--> ')
        if user_choice == 1:
            say_hello()
        elif user_choice == 2:
            hypotenuse()
        elif user_choice == 3:
            triangle()
        elif user_choice == 4:
            random_list()
        elif user_choice == 5:
            tupple_merge()
        elif user_choice == 6:
            most_popular()
        elif user_choice == 7:
            seconds()

def say_hello():
    name = input('Please insert your name: ').capitalize()
    surname = input('Please insert your surname: ').capitalize()
    age = input('Please insert your age: ')
    print(f'Hello {surname} {name}. Your age is {age}')


def hypotenuse():
    a = float(input('Please insert first triangle cathet: '))
    b = float(input('Please insert first triangle cathet: '))
    c = (a * a + b * b) ** 0.5
    print(f'Triangle hypotenuse equal: {c}')


def triangle():
    a = float(input('Please insert first triangle cathet: '))
    b = float(input('Please insert second triangle cathet: '))
    c = float(input('Please insert hypotenuse : '))
    if c ** 2 == a ** 2 + b ** 2:
        print('This is right triangle')
    else:
        print('This is not right triangle')

def random_list():
    randoms = []
    for i in range(4):
        randoms.append(input('Please insert random value 4 times: '))
    randoms.reverse()
    for g in randoms:
        print(g)


def tupple_merge():
    a = (1, 2, 3, 5, 8)
    b = (8, 2, 5)
    new_tuple = a[0:2]
    new_tuple2 =a[2:5]
    new_tuple3 = new_tuple + b + new_tuple2
    print(new_tuple3)



def most_popular():
    list1 = [1, 2, 4, 6, 4, 6]
    print(max(set(list1), key = list1.count))


def seconds():
    sec_value = int(input('Please insert value: '))
    a = sec_value % 60
    b = sec_value//60 % 60
    c = sec_value//3600 % 24
    d = sec_value//86400
    print(f'{d}:{c}:{b}:{a}')

menu()


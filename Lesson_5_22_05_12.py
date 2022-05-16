# x = 5
#
# student = {'name': 'John', 'age': 32, 'courses': ['Math', 'Biology', 'Art'], 1: 'int_key', 0.2: 'float_ key',
#             x: 'variable', 'var_value': x}
#
#
# print(student['name'])
# print(student.get('surname', 'Didn\'t find'))
#
# student['name'] = 'Bob'
# student['phone'] = '555-555-555'
#
# for x in range(10):
#     student[str(x)] = x ** 2
#
# print(student)
#
# student2 = {'name': 'Bob', 'age': 25, 'phone': '56832155'}
#
# student.update(student2)
#
# print(student)
#
# del student['name']
#
# print(student)
# print(student.keys())
# print(student.values())
# print(student.keys())
#
#
# x = 0
# # while x < 100:
# #     print(x)
# #     x +=  1
#
#
# current_position = 0
# finish_position = 1000
# step = 0.65
# step_cnt = 0
# while current_position < finish_position:
#     current_position += step
#     step_cnt += 1
# print(step_cnt, current_position)


user_input = input('Enter id:')

try:
    int(user_input)
except:
    print('Code is not numeric')
else:
    print(user_input)
finally:
    print('Good bye')
# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
print(example_string1.replace('Hello', 'Hero'))

# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
print(example_string2.lower().capitalize())


# Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"
print(example_string3.strip('*'))


# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"
print(example_string4.capitalize())


# Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(f'{var2.capitalize()}, {var3.lower()} {var1.capitalize()}')


# Write a code to return byte_string text value
byte_string = b"\316\273"
print(byte_string.decode())

# Write a code to return True if cost is greater than 500$
example_string5 = "It cost me 1000.00$"

print(example_string5.rstrip('$').split()[3])
if int(float(example_string5.rstrip('$').split()[3])) > 500:
    print('True')
else:
    print('False')






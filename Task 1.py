a = float(input('Please enter something: '))
b = float(input('Please enter something: '))
c = float(input('Please enter something: '))

half_of_p = (a+b+c)/2
square =  (half_of_p * (half_of_p - a) * (half_of_p - b) * (half_of_p - c)) ** 0.5

print(square)


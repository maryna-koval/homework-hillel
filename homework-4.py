from math import sqrt
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
p = (a + b + c)/2
print(f'Triangle area is {sqrt(p*(p-a)*(p-b)*(p-c))}')

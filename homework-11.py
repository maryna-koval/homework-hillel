print('Завдання №1')
numbers = []
for i in range(5):
    number = int(input('Enter your number '))
    numbers.append(number)
print('Your list is:', *numbers)
print('Завдання №2')
A = [1, 2, 3, 4, 5]
A.pop()
print(*A)
print('Завдання №3')
B = []
for i in range(10):
    numbers = int(input('Enter your number '))
    B.append(numbers)
N = int(input('Enter new number '))
counter = B.count(N)
print(counter)
print('Завдання №4')
a = int(input('Enter length of the list '))
C = []
for i in range(a):
    numbers = int(input('Enter your number '))
    C.append(numbers)
C.reverse()
print(*C)
print('Завдання №5')
D = []
E = []
for i in range(5):
    numbers = int(input('Enter your number '))
    D.append(numbers)
for numbers in D:
    if numbers > 5:
        E.append(numbers)
print('Numbers > 5 are' *E)
print('Завдання №6')
k = int(input('Enter length of the list '))
F = []
for i in range(k):
    numbers = int(input('Enter your number '))
    F.append(numbers)
min_nb = F[0]
max_nb = F[0]
for numbers in F:
    if numbers < min_nb:
        min_nb = numbers
    if numbers > max_nb:
        max_nb = numbers
print("Min number is:", min_nb)
print("Max number is:", max_nb)
print('Завдання №7')
text = input('Enter your text ')
t = 0
for char in text:
    if char.isdigit():
        t += 1
print(t)

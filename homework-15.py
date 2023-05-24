import random
from collections import Counter
print('Завдання №1')
numbers = []
storage = ''
with open('random.txt', 'r') as f:
    for line in f:
        for char in line:
            if char.isdigit():
                storage += char
            elif storage:
                numbers.append(int(storage))
                storage = ''
if storage:
    numbers.append(int(storage))
print(numbers)

print('Завдання №2')
text = input('Enter your text ')
with open('data.txt', 'w') as t:
    t.write(str(text))

print('Завдання №3')
N = int(input('Enter length of the list '))
string = []
for i in range(N):
    k = int(input('Enter your number '))
    string.append(k)
new_string = ' '.join(str(k) for k in string)
with open('numbers.txt', 'w') as n:
    n.write(str(new_string))

print('Завдання №4')
my_list = [random.randint(1, 50) for x in range(100)]
list_in_colomn = '\n'.join(str(k) for k in my_list)
with open('random_numbers.txt', 'w') as p:
  p.write(str(list_in_colomn))

print('Завдання №5')
counter = 0
with open('random.txt', 'r') as m:
    for line in m:
        words = line.split()
        for word in words:
            counter += 1
print(f'You have {counter} words in your file')

print('Завдання №6')
with open('sum.txt', 'r') as h:
    numbers_str = h.read()
numbers_list = numbers_str.split()
numbers = [int(num) for num in numbers_list]
sum_of_numbers = sum(numbers)
print("Sum of numbers  is: ", sum_of_numbers)

print('Завдання №7')
with open('text.txt', 'r') as l:
    lines = l.readlines()
words = []
for line in lines:
    words.extend(line.strip().lower().split())
word_counts = Counter(words)
top_common = word_counts.most_common(5)
for word, count in top_common:
    print(f"'{word}' - {count} times")

print('Завдання№1')
A = {'John', 'Bob', 'Bill', 'Thomas', 'Erick', 'Sam'}
B = {'John', 'Thomas', 'Frank', 'Edmund', 'Tim'}

july_and_june = A.intersection(B)
result = ", ".join(july_and_june)
print("Імена боржників за Червень та Липень: " +result)

july = B.difference(A)
result2 = ", ".join(july)
print("Імена боржників за Липень: " + result2)

print('Завдання№2')
list_in_camel = ['FirstItem', 'FriendsList', 'MyTuple']
snake_case = []
for string in list_in_camel:
    new_string = ''
    for i, char in enumerate(string):
        if char.isupper() and i > 0:
            new_string += "_" + char.lower()
        else:
            new_string += char.lower()
    snake_case.append(new_string)
print(snake_case)
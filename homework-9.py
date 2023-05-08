password = input('Enter your password ')
score = 0
special_char = '+-/_%$#@!&*'
if len(password) >= 8:
    score += 1
else:
    print('The minimum password length is 8')
if any(char.isdigit() for char in password):
    score += 1
else:
    print('Use numbers')
if any(char.islower() for char in password):
    score += 1
else:
    print('Use small letters')
if any(char.isupper() for char in password):
    score += 1
else:
    print('Use capital letters')
if any(char in special_char for char in password):
    score += 1
else:
    print('Use special characters')
print(f'Password score = {score}')

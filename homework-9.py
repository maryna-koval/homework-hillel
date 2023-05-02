password = input('Enter your password ')
score = 0
if len(password) < 8:
    print('The minimum password length is 8')
else:
    score += 1
if password.isalpha():
    print('Use numbers')
else:
    score += 1
if password.islower():
    print('Use capital letters')
else:
    score += 1
if password.isupper():
    print('Use small letters')
else:
    score += 1
if password.__contains__('+'):
    score += 1
elif password.__contains__('-'):
    score += 1
elif password.__contains__('/'):
    score += 1
elif password.__contains__('_'):
    score += 1
elif password.__contains__('%'):
    score += 1
else:
    print('Use special characters')
print(f'score = {score}')

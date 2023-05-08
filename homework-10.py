print('Завдання №1')
word1 = input('Enter your word ')
if word1 == word1[::-1]:
    print("+")
else:
    print("-")
print('Завдання №2')
text = input('Enter your text ')
word2 = input('Enter your word ')
if word2.lower() in text.lower():
    print('YES')
else:
    print('NO')
print('Завдання №3')
string = input('Enter your string ')
if string.startswith('abc'):
    new_string = 'www' + string[3:]
else:
    new_string = string + 'qqq'
print(new_string)
print('Завдання №4')
text2 = input("Enter your text ")
digits = "0123456789"
new_text = ""
for char in text2:
    if char not in digits:
        new_text += char
print(new_text)
print('Завдання №5')
email = input('Enter your email ')
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')

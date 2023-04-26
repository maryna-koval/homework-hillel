n = int(input("Enter your number: "))

if n > 20 and n % 2 != 0:
    print('Not Weird')
elif n % 2 != 0:
    print('Weird')
elif n % 2 == 0 and 2 <= n <= 5:
    print('Not Weird')
elif 6 <= n <= 20 and n % 2 == 0:
    print('Weird')
else:
    print('Not in range')

N = int(input("Enter your number: "))
for i in range(N, 0, -1):
    print('*' * i)
print('\n')
for i in range(0, N+1, 1):
    print('*' * i)
print('\n')
for i in range(N, 0, -1):
    print(' ' * (N - i) + '*' * i)
print('\n')
for i in range(0, N+1, 1):
    print((N - i)*' ' + '*' * i)

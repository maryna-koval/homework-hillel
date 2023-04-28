N = int(input("Enter your number: "))
i = 0
b = 0
total_sum = 0
while i <= N:
    if i % 3 == 0:
        print(i)
    i += 1
while b <= N:
    if b % 3 == 0:
        total_sum += b
    b += 1
print(f'Total sum is {total_sum}')


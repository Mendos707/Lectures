primes = []
user_choice = int(input('Please enter range limit: '))

for num in range(1, user_choice + 1):
    cnt = 0
    if num == 0:
        primes.append(num)
    for x in range(1, num + 1):
        if num % x == 0:
            cnt += 1
    if cnt == 2:
        primes.append(num)


print(primes)
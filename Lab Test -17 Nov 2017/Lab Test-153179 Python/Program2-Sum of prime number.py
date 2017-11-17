def isPrime(num):
    j = 2
    primeFlag = True
    while(j<=num):
            if(num%j == 0 and j!=num):
                    primeFlag = False
            j= j + 1
    return primeFlag
sum = 0
for i in range(2, 43):
        if (isPrime(i)):
            sum += i

print('The sum of first 15 prime numbers is: ', sum)

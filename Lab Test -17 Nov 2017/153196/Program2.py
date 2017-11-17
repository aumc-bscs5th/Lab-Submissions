def isPrime(num):
    j = 2
    primeFlag = True
    while(j<=num):
        if(num%j == 0 and j!=num):
            primeFlag = False
        j = j + 1
    return primeFlag

sum = 0
for i in range(2, 48):
    if (isPrime(i)):
        sum += i
print 'Sum of first fifteen prime numbers are: ', sum

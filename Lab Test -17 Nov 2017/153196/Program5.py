num = input('Enter a number: ')
n = num
sum = 0
while (n != 0):
    x = n % 10
    n = n - x
    n = n / 10
    sum += x ** 3
if sum == num:
    print 'Number is Armstrong'
else:
    print 'Number is not Armstrong'

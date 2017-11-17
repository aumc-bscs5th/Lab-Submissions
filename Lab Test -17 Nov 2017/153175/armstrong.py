num = int(input("Enter a number to check if it is Armstrong"))
sum = 0
n= num
while n > 0:
   digit = n % 10
   sum += digit ** 3
   n //= 10
if num == sum:
   print(num,"Armstrong number")
else:
   print(num,"Not an Armstrong number")

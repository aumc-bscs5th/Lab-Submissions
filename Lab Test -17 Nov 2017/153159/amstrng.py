num = int(input("Enter a number to check Armstrong : "))
sum = 0
rNum= num
while rNum > 0:
   digit = rNum % 10
   sum += digit ** 3
   rNum //= 10

if num == sum:
   print num,'is an Armstrong number'
else:
   print num,'is not an Armstrong number'

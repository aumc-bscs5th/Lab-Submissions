
num = int(input("Enter a number: "))
sum = 0
tempnum = num
while tempnum > 0:
   digit = tempum % 10
   sum += digit ** 3
   tempnum //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
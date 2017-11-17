n = int(input("Enter a 3 digit number: "))

s = 0

t = n
while t > 0:
   d = t % 10
   s += d ** 3
   t //= 10


if n == s:
   print("is an Armstrong number")
else:
   print("is not an Armstrong number")
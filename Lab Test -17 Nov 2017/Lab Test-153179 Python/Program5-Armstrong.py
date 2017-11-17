num = int(raw_input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    num1 = temp%10
    sum += num1 ** 3
    temp //=10
if num ==sum:
    print("Num is armstong")
else:
    print("Not an armstong number")

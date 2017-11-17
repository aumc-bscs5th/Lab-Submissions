while True:
	print("Enter 'exit' for exit.")
	num = input("Enter any number: ")
	if num == 'exit':
		break
	else:
		number = int(num)
		orignal = number
		reverse = 0
		while number > 0:
			reverse = (reverse*10) + number%10
			number //= 10
		if orignal == reverse:
			print(orignal, "is a Palindrome Number.\n")
		else:
			print(orignal, "is not a Palindrome Number.\n")


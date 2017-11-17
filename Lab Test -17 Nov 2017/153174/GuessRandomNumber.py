import random
num = random.randint(1,50)

while NumGuessed != num :
	NumGuessed = int(input("Enter a number to guess the computer's random number: "))
	if (NumGuessed==num):
		print("You won, you guess the number, what a LUCK :D ")
	else:
                print("Try Again, you can guess it :D ")

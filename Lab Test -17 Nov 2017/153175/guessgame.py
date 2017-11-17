guessed=False
while guessed==False:
    userInput = int(input("Your guess: "))
    import random
    randomNumber = random.randrange(0,50)
    print("Random number in entered")

    if userInput==randomNumber:
        guessed = True
        print("Wow great!")
    elif userInput>50:
        print("Guessed number should be less than 50.Enter again")
    elif userInput<0:
        print("Guess range should be greater than 0.Enter again")
    elif userInput!=randomNumber:
        print ('Try again , guessed number was', randomNumber)


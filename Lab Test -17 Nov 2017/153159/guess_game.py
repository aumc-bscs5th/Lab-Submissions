guessed=False
while guessed==False:
    userInput = int(input("Your guess please: "))
    import random
    randomNumber = random.randrange(0,50)
    print("Random number has been generated")

    if userInput==randomNumber:
        guessed = True
        print("Well done!")
    elif userInput>50:
        print("Our guess range is between 0 and 50, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 50, please try a bit higher")
    elif userInput!=randomNumber:
        print'Try one more time , generated number was', randomNumber


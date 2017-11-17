import random
num = random.randint(1 ,50)
guessNum = input("Enter your guss number: ")
flag = True
while flag:
    if (guessNum == num):
        flag = False
        print('Wow! you have guess right number!')
    elif(guessNum > num):
        print('Hint: You have guess number is greater than actual number.')
        guessNum = input("Guess again! Number a number: ")
    elif(guessNum < num):
        print('Hint: You have guess number is less than actual number.')
        guessNum = input("Guess again! Number a number: ")
    else:
        continue

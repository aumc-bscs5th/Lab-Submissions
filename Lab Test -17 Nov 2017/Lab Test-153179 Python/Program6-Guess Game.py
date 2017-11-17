import random
i = 0
num = random.randint(1, 50)
print ("I'm thinking of an number between 1 and 50. Guess it!")
while (i == 0):
     theGuess = int(raw_input("Your guess: "))
     if theGuess == num:
          print ("Great Job! Number has matched")
          i = 1
     else:
          print "Number not matched.Try Again :P ."

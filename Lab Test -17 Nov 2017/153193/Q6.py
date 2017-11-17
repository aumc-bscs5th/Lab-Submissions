from random import randint
a=randint(0, 9)

print('lets play a game  i have a number in a variable gess it or u die \n\n')

i = input('\t\tgess the number\t\t')

if (i==a):
  print('you win ur life')
  
else:
  print('u will die\n\n the number was',a)

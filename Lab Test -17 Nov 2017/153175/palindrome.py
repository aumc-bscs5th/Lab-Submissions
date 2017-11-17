mystr = input("Input the string or number to check: ")

revstr = reversed(mystr)

if list(mystr) == list(revstr):
   print("Palindrome")
else:
   print("Not Palindrome")

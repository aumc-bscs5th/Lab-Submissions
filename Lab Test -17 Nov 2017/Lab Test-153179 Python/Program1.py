mystr=raw_input("Enter a number or string")
revstr = reversed(mystr)# reverse the string
if list(mystr) == list(revstr): # check if the string is equal to its reverse
   print("It is palindrome")
else:
   print("It is not palindrome")

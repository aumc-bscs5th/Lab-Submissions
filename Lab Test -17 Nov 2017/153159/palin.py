myStr = raw_input("Enter a number or string :")
rStr= reversed(myStr)
if list(myStr)==list(rStr):
    print ("It's a palindrome")
else:
    print ("It's not a palindrome")

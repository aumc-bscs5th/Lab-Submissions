myStr=raw_input("Enter a string : ")
str1= myStr.lower()
vowels = 0
for x in str1:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        vowels += 1
        print 'The vowels found are: ' ,x
print 'Number of vowels found: ' ,vowels

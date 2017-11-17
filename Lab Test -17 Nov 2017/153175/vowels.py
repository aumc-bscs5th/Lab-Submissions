num=input("Input the string to check vowels: ")
n = num
vowels = 0
for x in n:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        vowels += 1
        print ("The vowels are: "+str(x))
print ("Number of vowels are: "+str(vowels))

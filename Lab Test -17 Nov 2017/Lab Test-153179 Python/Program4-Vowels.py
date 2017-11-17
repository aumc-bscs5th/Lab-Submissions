import string
string_a="abcdefghijklmnopqrstuvwxyz"
i=0
b="q"
for c in string_a:
        b=c
        if(b=="a"):
                i=i+1
        if(b=="e"):
                i=i+1
        if(b=="i"):
                i=i+1
        if(b=="o"):
                i=i+1
        if (b=="u"):
                i=i+1
print("Number of vowels are ", i)

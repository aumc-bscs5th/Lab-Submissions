inputString = str(input("Please type a sentence: "))
a = "a"
A = "A"
e = "e"
E = "E"
i = "i"
I = "I"
o = "o"
O = "O"
u = "u"
U = "U"
acount = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0

if A or a in stri :
     acount = acount + 1

if E or e in stri :
     ecount = ecount + 1

if I or i in stri :
    icount = icount + 1

if o or O in stri :
     ocount = ocount + 1

if u or U in stri :
     ucount = ucount + 1

print(acount + ecount + icount + ocount + ucount)
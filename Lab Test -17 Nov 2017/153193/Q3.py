a = [1, 2, 5, 7,9 ,24]
b = [2, 5, 7, 9,23]

for e in b:
        if e not in a:
            a.append(e)

print (a)
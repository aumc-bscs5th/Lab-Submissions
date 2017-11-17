i=1
sum=0
x = int(50)
for k in range (1, (x+1), 1):
    c=0
    for j in range (1, (i+1), 1):
        a = i%j
        if (a==0):
            c = c+1

    if (c==2):
          sum+=i
          print (sum)
    else:
          k = k-1

    i=i+1

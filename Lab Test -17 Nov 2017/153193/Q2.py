import numpy as np  

num = 50 
v=0

for a in range(2,num+1):         
  maxInt=int(np.sqrt(a)) + 1  
  for i in range(2,maxInt):
    if (a%i==0):  
      break  
  else: 
    print (a)
    v=v+a
        
   

print ("\nthe sum of first 15 prime number is  ",v,"\n\n")
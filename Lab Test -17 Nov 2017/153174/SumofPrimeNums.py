Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> sum=0
>>> limit=50
>>> for n in range(2,limit+1):
	if all(n % i for i in range(2, n)):
		sum += n
		print (sum)

		
2
5
10
17
28
41
58
77
100
129
160
197
238
281
328
>>> 

Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = input("What is your name?     ")
What is your name?     Umar
>>> name
'Umar'
>>> age = input("What is your age in yrs?      ")
What is your age in yrs?      23
>>> age
'23'
>>> str(age)
'23'
>>> print ("You will be 100 in ",100-age," years")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print ("You will be 100 in ",100-age," years")
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> print ("You will be 100 in ",int(100-age)," years")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print ("You will be 100 in ",int(100-age)," years")
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> age = int(input("What is your age in yrs?      "))
What is your age in yrs?      23
>>> type(age)
<class 'int'>
>>> print ("You will be 100 in ",int(100-age)," years")
You will be 100 in  77  years
>>> print ("The year will be",2017+int(100-age)," !!!!")
The year will be 2094  !!!!
>>> 

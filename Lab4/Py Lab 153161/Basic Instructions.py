Python 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> In[19]

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    In[19]
NameError: name 'In' is not defined
>>> In[19]:
	
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> x = 1
>>> type x
SyntaxError: invalid syntax
>>> type(x)
<type 'int'>
>>> ##
>>> ##################
>>> x =1.0
>>> type(x)
<type 'float'>
>>> ##################
>>> b1 = true

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b1 = true
NameError: name 'true' is not defined
>>> b1 = True
>>> b2 = False
>>> type (b1)
<type 'bool'>
>>> 
>>> ##########################
>>> x = 1.0-1.0j
>>> type(x)
<type 'complex'>
>>> ##########################
>>> 
>>> 
>>> print x
(1-1j)
>>> print(x.real,x.imag)
(1.0, -1.0)
>>> # print all types defined in the TYPE modules
>>> print(dir(types))

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(dir(types))
NameError: name 'types' is not defined
>>> print(dir(type))
['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__', '__dictoffset__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__weakrefoffset__', 'mro']
>>> #######################################
>>> x = 1.0
>>> type(x)
<type 'float'>
>>> type(x)is int
False
>>> #######################################
>>> isinstance(x,float)
True
>>> x = 1.5
>>> print(x,type(x))
(1.5, <type 'float'>)
>>> #######################################
>>> z = complex(x)
>>> print(z,type(z))
((1.5+0j), <type 'complex'>)
>>> x=float(z)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    x=float(z)
TypeError: can't convert complex to float
>>> y = bool(z.real)
>>> y = bool(z.imag)
>>> print(z.imag,"->",y,type(y))
(0.0, '->', False, <type 'bool'>)
>>> #######################################
>>> 
>>> 
>>> 
>>> 1 + 2,1-2,1*2,1/2
(3, -1, 2, 0)
>>> 1.0+2.0,1.0-2.0,1.0*2.0,1.0/2.0
(3.0, -1.0, 2.0, 0.5)
>>> ########################################
>>> #integer division of sloat numbers
>>> 3.0//2.0
1.0
>>> #power
>>> 2**4
16
>>> True and Flase

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    True and Flase
NameError: name 'Flase' is not defined
>>> True and False
False
>>> not False
True
>>> True or False
True
>>> ###########Comparisob Operators########
>>> 2>1.2<1
False
>>> 2>1,2<1
(True, False)
>>> 2>2,2<2
(False, False)
>>> ############EQUALITY#####################
>>> [1,2]==[1,2]
True
>>> ###########IDENTICAL OBJECTS##############
>>> I1 = I2 = [1,2]
>>> I1 is I2
True
>>> 

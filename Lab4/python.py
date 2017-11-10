Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #integers
>>> x = 1
>>> type(x)
<class 'int'>
>>> #float
>>> x = 1.0
>>> type(x)
<class 'float'>
>>> #boolean
>>> b1 = true
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b1 = true
NameError: name 'true' is not defined
>>> b1 = "true"
>>> b2 = "false"
>>> type(b1)
<class 'str'>
>>> # complex numbers: note the use of `j` to specify the imaginary part
>>> x = 1.0-1.0j
>>> type(x)
<class 'complex'>
>>> print(x)
(1-1j)
>>> print(x.real,x.image)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(x.real,x.image)
AttributeError: 'complex' object has no attribute 'image'
>>> print(x.real,x.imag)
1.0 -1.0
>>> import types
>>> #print all types defined in the types module
>>> print(dir(types))
['AsyncGeneratorType', 'BuiltinFunctionType', 'BuiltinMethodType', 'CodeType', 'CoroutineType', 'DynamicClassAttribute', 'FrameType', 'FunctionType', 'GeneratorType', 'GetSetDescriptorType', 'LambdaType', 'MappingProxyType', 'MemberDescriptorType', 'MethodType', 'ModuleType', 'SimpleNamespace', 'TracebackType', '_GeneratorWrapper', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_ag', '_calculate_meta', '_collections_abc', '_functools', 'coroutine', 'new_class', 'prepare_class']
>>> ['AsyncGeneratorType', 'BuiltinFunctionType', 'BuiltinMethodType', 'CodeType', 'CoroutineType', 'DynamicClassAttribute', 'FrameType', 'FunctionType', 'GeneratorType', 'GetSetDescriptorType', 'LambdaType', 'MappingProxyType', 'MemberDescriptorType', 'MethodType', 'ModuleType', 'SimpleNamespace', 'TracebackType', '_GeneratorWrapper', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_ag', '_calculate_meta', '_collections_abc', '_functools', 'coroutine', 'new_class', 'prepare_class']
['AsyncGeneratorType', 'BuiltinFunctionType', 'BuiltinMethodType', 'CodeType', 'CoroutineType', 'DynamicClassAttribute', 'FrameType', 'FunctionType', 'GeneratorType', 'GetSetDescriptorType', 'LambdaType', 'MappingProxyType', 'MemberDescriptorType', 'MethodType', 'ModuleType', 'SimpleNamespace', 'TracebackType', '_GeneratorWrapper', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_ag', '_calculate_meta', '_collections_abc', '_functools', 'coroutine', 'new_class', 'prepare_class']
>>> ['AsyncGeneratorType', 'BuiltinFunctionType', 'BuiltinMethodType', 'CodeType', 'CoroutineType', 'DynamicClassAttribute', 'FrameType', 'FunctionType', 'GeneratorType', 'GetSetDescriptorType', 'LambdaType', 'MappingProxyType', 'MemberDescriptorType', 'MethodType', 'ModuleType', 'SimpleNamespace', 'TracebackType', '_GeneratorWrapper', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_ag', '_calculate_meta', '_collections_abc', '_functools', 'coroutine', 'new_class', 'prepare_class']
['AsyncGeneratorType', 'BuiltinFunctionType', 'BuiltinMethodType', 'CodeType', 'CoroutineType', 'DynamicClassAttribute', 'FrameType', 'FunctionType', 'GeneratorType', 'GetSetDescriptorType', 'LambdaType', 'MappingProxyType', 'MemberDescriptorType', 'MethodType', 'ModuleType', 'SimpleNamespace', 'TracebackType', '_GeneratorWrapper', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_ag', '_calculate_meta', '_collections_abc', '_functools', 'coroutine', 'new_class', 'prepare_class']
>>> x = 1.0
>>> # check if the variable x is a float
>>> type(x) is int
False
>>> #We can also use the isinstance method for testing types of variables:
>>> isinstance(x,float)
True
>>> #typecasting
>>> x = 1.5
>>> print(x,type(x))
1.5 <class 'float'>
>>> x = int(x)
>>> print(x,type(x))
1 <class 'int'>
>>> z = complex(x)
>>> print(z,type(z))
(1+0j) <class 'complex'>
>>> x = float(z)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    x = float(z)
TypeError: can't convert complex to float
>>> x = float(z)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x = float(z)
TypeError: can't convert complex to float
>>> y = bool(z.real)
>>> print(z.real, " -> ", y, type(y))
1.0  ->  True <class 'bool'>
>>> y = bool(z.imag)
>>> print(z.imag, " -> ", y, type(y))
0.0  ->  False <class 'bool'>
>>> #Arithmetic operators +, -, *, /, // (integer division), '**' power
>>> 1+2,1-2,1*2,1/2
(3, -1, 2, 0.5)
>>> 1.0 + 2.0, 1.0 - 2.0, 1.0 * 2.0, 1.0 / 2.0
(3.0, -1.0, 2.0, 0.5)
>>> # Integer division of float numbers
>>> 3.0//2.0
1.0
>>> # Note! The power operators in python isn't ^, but **
>>> 2**2
4
>>> 1/2
0.5
>>> true and false
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    true and false
NameError: name 'true' is not defined
>>> #The boolean operators are spelled out as the words and, not, or.
>>> True and False
False
>>> not False
True
>>> True or False
True
>>> #Comparison operators >, <, >= (greater or equal), <= (less or equal), == equality, is identical.
>>> 2 > 1, 2 < 1
(True, False)
>>> 2 > 2, 2 < 2
(False, False)
>>> 2 >= 2, 2 <= 2
(True, True)
>>> # equality
>>> [1,2] == [1,2]
True
>>> # objects identical?
>>> l1 = l2 = [1,2]
>>> l1 is l2
True
>>> --------------------# raw_input_example.py------------------------------
SyntaxError: invalid syntax
>>> #--------------------# raw_input_example.py------------------------------
>>> name = raw_input("What is your name? ")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    name = raw_input("What is your name? ")
NameError: name 'raw_input' is not defined
>>> name == raw_input("What is your name? ")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    name == raw_input("What is your name? ")
NameError: name 'name' is not defined
>>> name = input("What is your name? ")
What is your name? warda
>>> city = input("What city do you live in? ")
What city do you live in? multan
>>> state = input("What state is that in? ")
What state is that in? pakistan
>>> print "Hello there! It is so great to meet you,"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello there! It is so great to meet you,")?
>>> print ("Hello there! It is so great to meet you,")
Hello there! It is so great to meet you,
>>> # One way to do this is to print strings on separate lines
>>> print (name)
warda
>>> print("from")
from
>>> print(city)
multan
>>> print(state)
pakistan
>>> # We can also "glue together" pieces of a string by adding commas
# between them.
>>> print( name, "from", city, state)
warda from multan pakistan
>>> ## This doesn't work because raw_input returns a string
>>> #age = raw_input("Pardon my rudeness, but how old are you? ")
>>> #print "Wow! You look like you could be", age - (0.15*age), "!!"
>>> age = input("Pardon my rudeness, but how old are you? ")
Pardon my rudeness, but how old are you? 20
>>> print ("Wow! You look like you could be", int(age - (0.15*age)), "!!")
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print ("Wow! You look like you could be", int(age - (0.15*age)), "!!")
TypeError: can't multiply sequence by non-int of type 'float'
>>> print ("Wow! You look like you could be", (age - (0.15*age)), "!!")
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print ("Wow! You look like you could be", (age - (0.15*age)), "!!")
TypeError: can't multiply sequence by non-int of type 'float'
>>> print ("Wow! You look like you could be", float(age - (0.15*age)), "!!")
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    print ("Wow! You look like you could be", float(age - (0.15*age)), "!!")
TypeError: can't multiply sequence by non-int of type 'float'
>>> age = int(input("paradon my rudness,but how old are you"))
paradon my rudness,but how old are you 20
>>>  print ("Wow! You look like you could be", int(age - (0.15*age)), "!!")
 
SyntaxError: unexpected indent
>>>  print ("Wow! You look like you could be", int(age - (0.15*age)), "!!")
 
SyntaxError: unexpected indent
>>> print ("wow! you look like you could be", int(age - (0.15*age)), "!!")
wow! you look like you could be 17 !!
>>> # Examples of if statements
>>> if 9 > 5:
	print "Yes, 9 greater than 5"
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Yes, 9 greater than 5")?
>>> print ("Yes, 9 greater than 5")
Yes, 9 greater than 5
>>> if 9 != 5:
	print ("Yes, 9 not equal to 5")

	
Yes, 9 not equal to 5
>>> # An example of an if/else statemet
>>> #if 9 < 5:
>>> print ("Yes, 9 less than 5")
Yes, 9 less than 5
>>> else:
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> if 9 < 5:
	print ("Yes, 9 less than 5")
	else:
		
SyntaxError: invalid syntax
>>> else:
print ("No, 9 is not less than 5")
SyntaxError: invalid syntax
>>> if 9 < 5:
	print ("Yes, 9 less than 5")
	else:
		
SyntaxError: invalid syntax
>>> if 9 < 5:
	print ("Yes, 9 less than 5")
	if 9 < 5:




\
  
SyntaxError: expected an indented block
>>> 
>>> if 9 < 5:
	print ("Yes, 9 less than 5")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if 9 < 5:
	print ("Yes, 9 less than 5")if 9 < 5:
		print ("Yes, 9 less than 5")
		
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> if 9 < 5:
		print ("Yes, 9 less than 5")if 9 < 5:
			
SyntaxError: invalid syntax
>>> if 9 < 5:
		print ("Yes, 9 less than 5")
	else:
		
SyntaxError: unindent does not match any outer indentation level
>>> # Traffic light example
>>> light_color = input("What color is the traffic light? ")
What color is the traffic light? 
>>> 
>>>  # Traffic light example
 
>>> if light_color == "red":
		print ("You should stop")

		
>>> elif light_color == "yellow":
	
SyntaxError: invalid syntax
>>> name = input("what is your name")
what is your namewarda
>>> age = input("how old are you")
how old are you20
>>> print("100-age+2017")
100-age+2017
>>> 100-age+2017
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    100-age+2017
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> age=int(input("whats your age?")





	cold
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> ld
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    ld
NameError: name 'ld' is not defined
>>> 

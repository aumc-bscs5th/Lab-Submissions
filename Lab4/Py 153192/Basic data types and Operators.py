Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=1
>>> type(x)
<class 'int'>
>>> x=1.0
>>> type(x)
<class 'float'>
>>> b1=True
>>> b2=False
>>> type(b2)
<class 'bool'>
>>> x=1.0-1.0j
>>> type(x0)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type(x0)
NameError: name 'x0' is not defined
>>> type(x)
<class 'complex'>
>>> (1-1j)
(1-1j)
>>> print(x)
(1-1j)
>>> print(x.real,x.imag)
1.0 -1.0
>>> import type
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    import type
ModuleNotFoundError: No module named 'type'
>>> import types
>>> 
>>> print(dir(types))
['AsyncGeneratorType', 'BuiltinFunctionType', 'BuiltinMethodType', 'CodeType', 'CoroutineType', 'DynamicClassAttribute', 'FrameType', 'FunctionType', 'GeneratorType', 'GetSetDescriptorType', 'LambdaType', 'MappingProxyType', 'MemberDescriptorType', 'MethodType', 'ModuleType', 'SimpleNamespace', 'TracebackType', '_GeneratorWrapper', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_ag', '_calculate_meta', '_collections_abc', '_functools', 'coroutine', 'new_class', 'prepare_class']
>>> type(x) is int
False
>>> type(x) is float
False
>>> isinstance(x,float)
False
>>> x=1.5
>>> print(x,type(x))
1.5 <class 'float'>
>>> x=int(x)
>>> print(x,type(x))
1 <class 'int'>
>>> z=complex(x)
>>> print(z,type(z))
(1+0j) <class 'complex'>
>>> x=float(z)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x=float(z)
TypeError: can't convert complex to float
>>> y=bool(z.real)
>>> print(z.real,"->" y,type(y))
SyntaxError: invalid syntax
>>>  print(z.real,"->", y,type(y))
 
SyntaxError: unexpected indent
>>> print(z.real,"->" ,y,type(y))
1.0 -> True <class 'bool'>
>>> print(z.imag, " -> ", y, type(y))
0.0  ->  True <class 'bool'>
>>> 
>>> #Operators and comparisons
>>> 1 + 2, 1 - 2, 1 * 2, 1 / 2
(3, -1, 2, 0.5)
>>> 1.0 + 2.0, 1.0 - 2.0, 1.0 * 2.0, 1.0 / 2.0
(3.0, -1.0, 2.0, 0.5)
>>> 3.0 // 2.0
1.0
>>> 2 ** 2
4
>>> True and False
False
>>> not False
True
>>> True or False
True
>>> 2 > 1, 2 < 1
(True, False)
>>> 2 > 2, 2 < 2
(False, False)
>>> [1,2] == [1,2]
True
>>> l1 = l2 = [1,2]
>>> l1 is l2
True
>>> 

Python 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> name = raw_input("What is Your Name?")
What is Your Name?UMAR
>>> city = raw_input("What city do u live in?")
What city do u live in?MULTAN
>>> state = raw_input("What state is that in?")
What state is that in?PUNJAB, PAKISTAN
>>> 
>>> print"Hello there! It is so great to meet you,"
Hello there! It is so great to meet you,
>>> pritn name
SyntaxError: invalid syntax
>>> print name
UMAR
>>> print(name," from ", city, state)
('UMAR', ' from ', 'MULTAN', 'PUNJAB, PAKISTAN')
>>> print name,"from",city,state
UMAR from MULTAN PUNJAB, PAKISTAN
>>> age = input("Pardon my rudeness, But how old are you?")
Pardon my rudeness, But how old are you?

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    age = input("Pardon my rudeness, But how old are you?")
  File "<string>", line 0
    
   ^
SyntaxError: unexpected EOF while parsing
>>> s

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 1
1
>>> age = input("Pardon my rudeness, But how old are you?")
Pardon my rudeness, But how old are you?23
>>> print("WOW ! You look like You could be ",int(age-(0.15*age)),"!!")
('WOW ! You look like You could be ', 19, '!!')
>>> 

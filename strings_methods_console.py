Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "Hello world, This is Python"
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'hello world, this is python'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON'
>>> text.title()
'Hello World, This Is Python'
>>> text.capitalize()
'Hello world, this is python'
>>> text.swapcase()
'hELLO WORLD, tHIS IS pYTHON'
>>> text.count('o')
3
>>> text
'Hello world, This is Python'
>>> text.index('o')
4
>>> text.index('o',0)
4
>>> text.index('o',5)
7
>>> text.index('o',8)
25
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.rfind('o')
25
>>> text.rindex('o')
25
>>> text.count('o')
3
>>> text.count('i')
2
>>> text.count('h')
2
>>> text.startswith('The')
False
>>> text.startswith('A')
False
>>> text.startswith('H')
True
>>> text.endswith('?')
False
>>> text.endswith('n')
True
>>> text.isalnum()
False
>>> text.isalpha()
False
>>> text.isascii()
True
>>> text.isupper()
False
>>> text.replace('hello', 'bye')
'Hello world, This is Python'
>>> text.replace('Hello', 'bye')
'bye world, This is Python'
>>> text.lower().replace('hello', 'bye')
'bye world, this is python'
>>> text.split()
['Hello', 'world,', 'This', 'is', 'Python']
>>> text.center(10)
'Hello world, This is Python'
>>> text.center(20)
'Hello world, This is Python'
>>> text.center(30)
' Hello world, This is Python  '
>>> len(text)
27
>>> text.center(26)
'Hello world, This is Python'
>>> text.center(27\)
	    
SyntaxError: unexpected character after line continuation character
>>> text.center(27)
'Hello world, This is Python'
>>> text.center(28)
'Hello world, This is Python '
>>> text.center(29)
' Hello world, This is Python '
>>> text.center(30)
' Hello world, This is Python  '
>>> text.center(31)
'  Hello world, This is Python  '
>>> text.center(41)
'       Hello world, This is Python       '
>>> text.center(41, '*')
'*******Hello world, This is Python*******'
>>> text = text.center(41)
>>> text
'       Hello world, This is Python       '
>>> text.strip()
'Hello world, This is Python'
>>> text.lstrip()
'Hello world, This is Python       '
>>> text.rstrip()
'       Hello world, This is Python'
>>> text = text.strip()
>>> text = text.center(41, '*')
>>> text
'*******Hello world, This is Python*******'
>>> text.strip()
'*******Hello world, This is Python*******'
>>> text.strip('*')
'Hello world, This is Python'
>>> 
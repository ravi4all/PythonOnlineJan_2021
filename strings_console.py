Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world, this is python programming"
>>> text[0] # index
'h'
>>> text[-1] # index
'g'
>>> len(text) # to find length of string
39
>>> text[30]
'o'
>>> text[31]
'g'
>>> text[0:5] # slicing of string [index : pos]
'hello'
>>> text[0:4]
'hell'
>>> text[0:30]
'hello world, this is python pr'
>>> text[0:30:2] # [index : pos : step]
'hlowrd hsi yhnp'
>>> text[10:0]
''
>>> text[10:0:-1] # to reverse a string set step = -1
'dlrow olle'
>>> text[0:20]
'hello world, this is'
>>> text
'hello world, this is python programming'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-10:-1]
'rogrammin'
>>> text[:]
'hello world, this is python programming'
>>> text[10:]
'd, this is python programming'
>>> text[:20]
'hello world, this is'
>>> text[::-1]
'gnimmargorp nohtyp si siht ,dlrow olleh'
>>> 
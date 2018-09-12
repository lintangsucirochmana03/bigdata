Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'spam eggs'
'spam eggs'
>>> 'doesn\'t'
"doesn't"
>>> "doesn't"
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> '"Isn\'t," they  said.'
'"Isn\'t," they  said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'Firt line.\nSecond line.'
>>> s
'Firt line.\nSecond line.'
>>> print(s)
Firt line.
Second line.
>>> print('C:some\name')
C:some
ame
>>> print(r'C:\some\name')
C:\some\name
>>> print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

>>> # 3 times 'un', folowwed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
>>> 'Py' 'thon'
'Python'
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
SyntaxError: invalid syntax
>>> text
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    text
NameError: name 'text' is not defined
>>> text = ('Put several strings within parentheses '
	    'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
>>> prefix = 'Py'
>>> prefix 'thon'
SyntaxError: invalid syntax
>>> prefix 'thon'
SyntaxError: invalid syntax
>>> prefix + 'thon'
'Python'
>>> word = 'Python'

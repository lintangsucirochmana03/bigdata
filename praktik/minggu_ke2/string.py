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
>>> word[0]
'P'
>>> word[5]
'n'
>>> word[-1]
'n'
>>> word[-2] #secon-last character
'o'
>>> word[6]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    word[6]
IndexError: string index out of range
>>> word[-6]
'P'
>>> word[0:2] #character from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]
'tho'
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
>>> word[:2]
'Py'
>>> word[4:]
'on'
>>> word[-2:]
'on'
>>> word[42]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    word[42]
IndexError: string index out of range
>>> word[4:42]
'on'
>>> word[42:]
''
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    word[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> word[2:]
'thon'
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    word[2:] = 'py'
TypeError: 'str' object does not support item assignment
>>> "J + word[1:]
SyntaxError: EOL while scanning string literal
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
>>> s = 'supercalifragilisticexpialidocious'
>>> lens (s)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    lens (s)
NameError: name 'lens' is not defined
>>> len(s)
34
>>> l = lintang
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    l = lintang
NameError: name 'lintang' is not defined
>>> l ='lintang'
>>> len(l)
7
>>> 

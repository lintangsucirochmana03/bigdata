Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def ask_ok(prompt, retries=4, reminder='Please try again!'):
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)

		
>>> ok
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ok
NameError: name 'ok' is not defined
>>> y
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> return ok
SyntaxError: 'return' outside function
>>> i = 5
>>> def f(arg=i):
	print(arg)

	
>>> i = 6
>>> f()
5
>>> def f(a, L=[]):
	L.append(a)
	return L
print(f(1))
SyntaxError: invalid syntax
>>> def f(a, L=[]):
	L.append(a)
	return L

>>> print(f(1))
[1]
>>> print(f(2))
[1, 2]
>>> print(f(3))
[1, 2, 3]
>>> def f(a, L=None):
	if L is None:
		L = []
	L.append(a)
	return L

>>> 
>>> return L
SyntaxError: 'return' outside function
>>> 

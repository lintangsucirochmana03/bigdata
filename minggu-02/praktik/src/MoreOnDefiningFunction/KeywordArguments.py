Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.")
	print("-- Lovely plumage, the", type)
	print("-- It's", state, "!")

	
>>> parrot(1000)
-- This parrot wouldn't voom if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !
>>> parrot(voltage=1000)
-- This parrot wouldn't voom if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !
>>> parrot(voltage=1000000, action='VOOOOOM')
-- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !
>>> parrot(action='VOOOOOM', voltage=1000000)
-- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !
>>> parrot('a million', 'bereft of life', 'jump')
-- This parrot wouldn't jump if you put a million volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's bereft of life !
>>> parrot('a thousand', state='pushing up the daisies')
-- This parrot wouldn't voom if you put a thousand volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's pushing up the daisies !
>>> parrot()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    parrot()
TypeError: parrot() missing 1 required positional argument: 'voltage'
>>> parrot(voltage=5.0, 'dead')
SyntaxError: positional argument follows keyword argument
>>> parrot(110, voltage=220)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    parrot(110, voltage=220)
TypeError: parrot() got multiple values for argument 'voltage'
>>> parrot(actor='John Cleese')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    parrot(actor='John Cleese')
TypeError: parrot() got an unexpected keyword argument 'actor'
>>> def function(a):
	pass

>>> function(0, a=0)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    function(0, a=0)
TypeError: function() got multiple values for argument 'a'
>>> def cheeseshop(kind, *arguments, **keywords):
	print("-- Do you have any", kind, "?")
	print("-- I'm sorry, we're all out of", kind)
	for arg in arguments:
		print(arg)
	print("-" * 40)
	for kw in keywords:
		print(kw, ":", keywords[kw])

		
>>> cheeseshop("Limburger", "It's very runny, sir.",
	       "It's really very, VERY runny, sir.",
	       shopkeeper="Michael Palin",
	       client="John Cleese",
	       sketch="Cheese Shop Sketch")
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
>>> 

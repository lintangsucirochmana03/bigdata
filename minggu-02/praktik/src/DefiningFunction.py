Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def fib(n):    # write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b

		
>>> print()

>>> # Now call the function we just defined:
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
>>> fib
<function fib at 0x02C4CE88>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89 
>>> fib(0)
>>> print(fib(0))
None
>>> def fib2(n):  # return Fibonacci series up to n
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)    # see below
		a, b = b, a+b
	return result

>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> 

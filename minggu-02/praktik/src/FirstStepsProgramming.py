Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a , b = 0, 1
>>> while a < 10:
	print(a)
	a, b = b, a+b

	
0
1
1
2
3
5
8
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
>>> a, b = 0,1
>>> while a < 1000:
	print(a, end=',')
	a, b = b, a+b

	
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
>>> 

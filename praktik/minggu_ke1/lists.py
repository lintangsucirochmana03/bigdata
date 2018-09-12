Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> squares = [1, 4, 9, 25]
>>> squares
[1, 4, 9, 25]
>>> squares [0]
1
>>> squares[-1]
25
>>> squares[-3:]
[4, 9, 25]
>>> squares[:]
[1, 4, 9, 25]
>>> squares + [36,49,64,81,100]
[1, 4, 9, 25, 36, 49, 64, 81, 100]
>>> cubes = [1,8,27,65,125]
>>> 4 ** 3
64
>>> cubes[3] = 64
>>> cubes
[1, 8, 27, 64, 125]
>>> cube.append(216)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    cube.append(216)
NameError: name 'cube' is not defined
>>> cubes.append(216)
>>> cubes.append(7 ** 3)
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>> letters = ['a','b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letter[2:5] = []
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    letter[2:5] = []
NameError: name 'letter' is not defined
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
>>> lettters = ['a', 'b', 'c' ,'d']
>>> len(letters)
0
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
>>> 

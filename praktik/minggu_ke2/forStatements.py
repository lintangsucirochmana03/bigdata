Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Measure some strings:
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
	print(w, len(w))

	
cat 3
window 6
defenestrate 12
>>> for w in words[:]:  # Loop over a slice copy of the entire list.
	if len(w) > 6:
		words.insert(0, w)

		
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
>>> 

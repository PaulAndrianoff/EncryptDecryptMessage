from libs.mathFunction import coprime
from libs.settings import alphabetUrl, keysUrl

myKeys = []
alphaContent = open(alphabetUrl,'r').readlines()[0]
alphaLen = len(alphaContent)
verify = False

try:
	file = open(keysUrl,'r')
	currentFile = file.readlines()

	a = int(currentFile[0].split('\n')[0]) # a must be an integer coprim with alphabet length
	b = int(currentFile[1].split('\n')[0]) # any inter
	keyWord = currentFile[2].split('\n')[0] # any string that characters are in alphabet
	file.close()
	
	# Test if a == b 
	if (a == b): 
		a, b = a + 1, 0

	# Test if alphaLen and a are coprime
	if (coprime(alphaLen, a)):
		myKeys.append(a)
		myKeys.append(b)
		myKeys.append(keyWord)
		verify = True
	else:
		raise ValueError("Your first number is wrong: pgcd(" + str(alphaLen) + ", " + str(a) + ") = " + str(coprime(alphaLen, a)) )
	file.close()
		
except Exception as e:
	print(e)
from libs.mathFunction import coprime
from libs.settings import alphabetUrl, keysUrl

myKeys = []
alphaContent = open(alphabetUrl,'r').readlines()[0]
alphaLen = len(alphaContent)
verify = False

try:
	file = open(keysUrl,'r')
	currentFile = file.readlines()

	a = int(currentFile[0].split('\n')[0])
	b = int(currentFile[1].split('\n')[0])
	
	file.close()
	
	# Test if a == b 
	if (a == b): 
		a, b = a + 1, 0

	# Test if alphaLen and a are coprime
	if (coprime(alphaLen, a)):
		myKeys.append(a)
		myKeys.append(b)
		verify = True
	else:
		raise ValueError("Your first number is wrong: pgcd(" + str(alphaLen) + ", " + str(a) + ") = " + str(coprime(alphaLen, a)) )
	file.close()
		
except Exception as e:
	print(e)
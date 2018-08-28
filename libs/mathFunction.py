# Greater common diviser
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

def coprime(a, b):
	return gcd(a, b) == 1

# Bezute Couple
def bezuteCode(key, alphaLen):
	try:
		a = key
		b = alphaLen
		u, v = 1, 0
		u1, v1 = 0, 1

		while b != 0:
			q = int(a/b)
			
			tempA, tempU, tempV = a, u, v
			a, u, v = b, u1, v1

			b = tempA - q*b
			u1 = tempU - q*u1
			v1 = tempV - q*v1
		
		return u
	except Exception as e:
		return e

def setKeyWordMessage(message, keyWord):
	keyWordMessage = ''
	while len(message) > len(keyWordMessage):
		keyWordMessage = keyWordMessage + keyWord

	return keyWordMessage[0:len(message)]	
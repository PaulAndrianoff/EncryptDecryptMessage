test = 'mon super message de la mort.'
alphabet = "abcdefghijklmnopqrstuvwxyz "
word = 'je fais un super test'

wordTest = ''

def encryptLetter(letter1, letter2):
	try:
		return alphabet[(alphabet.index(letter1) + alphabet.index(letter2))%len(alphabet)]
	except:
		return letter1

def encryptWord(word):
	encryptMessage = ''
	i = 0
	while i < len(test):
		encryptMessage = encryptMessage + encryptLetter(word[i], wordTest[i])
		i = i + 1
	return(encryptMessage)

def decryptLetter(letter1, letter2):
	try:
		return alphabet[(alphabet.index(letter1) - alphabet.index(letter2))%len(alphabet)]
	except:
		return letter1

def decryptWord(word):
	decryptMessage = ''
	i = 0
	while i < len(test):
		decryptMessage = decryptMessage + decryptLetter(word[i], wordTest[i])
		i = i + 1
	return(decryptMessage)

while len(test) > len(wordTest):
	wordTest = wordTest + word

wordTest = wordTest[0:len(test)]

print(alphabet)
print(test)
print(wordTest)

encrypt = encryptWord(test)
print(encrypt)
print(decryptWord(encrypt))
from libs.verification import alphaLen, myKeys, verify, alphaContent
from libs.mathFunction import setKeyWordMessage

############################################
# Affine

def encrypteAffineLetter(letter):
	try:
		a = myKeys[0]
		b = myKeys[1]
		m = alphaLen
		currentIndex = alphaContent.index(letter)

		newIndex = (a * currentIndex + b)%m
		newLetter = alphaContent[newIndex]

		# print(letter + " - " + str(currentIndex) + " : " + newLetter + " - " + str(newIndex))
		return newLetter
	except Exception as e:
		return letter


def encrypteAffineMessage(message):
	newMessage = ""
	print('In encryption...')
	for letter in message:
		newMessage = newMessage + encrypteAffineLetter(letter)
	return newMessage

############################################
# Vigener

def encryptVigenerLetter(letter1, letter2):
	try:
		return alphaContent[(alphaContent.index(letter1) + alphaContent.index(letter2))%alphaLen]
	except:
		return letter1

def encryptVigenerWord(message):
	newMessage = ''
	i = 0
	KeyWordMessage = setKeyWordMessage(message, myKeys[2])
	while i < len(message):
		newMessage = newMessage + encryptVigenerLetter(message[i], KeyWordMessage[i])
		i = i + 1
	return(newMessage)

##############################
# Encryprion level control

def encrypteMessage(message):
	newMessage = ""
	if verify:
		newMessage = encrypteAffineMessage(message)
		newMessage = encryptVigenerWord(newMessage)
		return newMessage
	else:
		return "Sorry your message can't be encrypted"
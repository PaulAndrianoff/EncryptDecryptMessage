from libs.verification import alphaLen, myKeys, verify, alphaContent

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

##############################
# Encryprion level control

def encrypteMessage(message):
	newMessage = ""
	if verify:
		newMessage = encrypteAffineMessage(message)
		return newMessage
	else:
		return "Sorry your message can't be encrypted"
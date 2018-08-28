from libs.verification import alphaLen, myKeys, verify, alphaContent
from libs.mathFunction import bezuteCode, setKeyWordMessage

############################################
# Affine

def decrypteAffineLetter(letter):
	try:
		m = alphaLen
		a = bezuteCode(myKeys[0], alphaLen)
		b = myKeys[1]

		currentIndex = alphaContent.index(letter)

		newIndex = (a * (currentIndex - b))%m
		newLetter = alphaContent[newIndex]

		# print(letter + " - " + str(currentIndex) + " : " + newLetter + " - " + str(newIndex))
		return newLetter
	except:
		return letter


def decrypteAffineMessage(message):
	newMessage = ""
	for letter in message:
		newMessage = newMessage + decrypteAffineLetter(letter)
	return newMessage

############################################
# Vigener

def decryptVigenerLetter(letter1, letter2):
	try:
		return alphaContent[(alphaContent.index(letter1) - alphaContent.index(letter2))%alphaLen]
	except:
		return letter1

def decryptVigenerWord(message):
	newMessage = ''
	i = 0
	KeyWordMessage = setKeyWordMessage(message, myKeys[2])
	while i < len(message):
		newMessage = newMessage + decryptVigenerLetter(message[i], KeyWordMessage[i])
		i = i + 1
	return(newMessage)

##############################
# Encryprion level control
def decrypteMessage(message):
	newMessage = ""
	if verify:
		newMessage = decryptVigenerWord(message)
		newMessage = decrypteAffineMessage(newMessage)
		return newMessage
	else:
		return "Sorry your message can't be encrypted"
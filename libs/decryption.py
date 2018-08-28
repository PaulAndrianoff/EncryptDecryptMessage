from libs.verification import alphaLen, myKeys, verify, alphaContent
from libs.mathFunction import bezuteCode

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

##############################
# Encryprion level control
def decrypteMessage(message):
	newMessage = ""
	if verify:
		newMessage = decrypteAffineMessage(message)
		return newMessage
	else:
		return "Sorry your message can't be encrypted"
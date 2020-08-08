from libs.verification import alphaLen, myKeys, verify, alphaContent
from libs.mathFunction import bezuteCode, setKeyWordMessage, roundNum, randString
from libs.sysCommand import clear
import time

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
	i = 0
	maxLen = len(message)
	print("\n[", end='')
	for letter in message:
		time.sleep(0)
		newMessage = newMessage + decrypteAffineLetter(letter)
		if int(i/maxLen*100) % 10 == 0:
			print("#", end='')
		i += 1
	print('] \n Done')
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

############################################
# Remove random letter

def removeString(message):
	a = myKeys[0] + myKeys[1]
	b = len(myKeys[2])
	i = 0
	message = message[b:]
	message = message[:-b]
	while i < len(message):
		if (i%a == 0):
			message = message[:i+1] + message[i+b+1:]
		i = i + 1
	return message

##############################
# Encryprion level control
def decrypteMessage(message):
	newMessage = ""
	if verify:
		newMessage = removeString(message)
		newMessage = decryptVigenerWord(newMessage)
		newMessage = decrypteAffineMessage(newMessage)
		return newMessage
	else:
		return "Sorry your message can't be encrypted"
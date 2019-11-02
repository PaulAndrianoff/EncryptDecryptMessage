from libs.verification import alphaLen, myKeys, verify, alphaContent
from libs.mathFunction import setKeyWordMessage, randString
from libs.sysCommand import clear
import time

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
		
		return newLetter
	except Exception as e:
		return letter


def encrypteAffineMessage(message):
	newMessage = ""
	i = 0
	maxLen = len(message)
	print("\n[", end='')
	for letter in message:
		time.sleep(0)
		newMessage = newMessage + encrypteAffineLetter(letter)
		if int(i/maxLen*100) % 10 == 0:
			print("#", end='')
		i += 1
	print('] \n Done')
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

############################################
# Add random letter

def addString(message):
	a = myKeys[0] + myKeys[1]
	b = len(myKeys[2])
	newMessage = randString(b, alphaContent)
	i = 0
	while i < len(message):
		newMessage = newMessage + message[i]
		if (i%a == 0):
			newMessage = newMessage + randString(b, alphaContent)
		i = i + 1
	newMessage = newMessage + randString(b, alphaContent)
	return newMessage

##############################
# Encryprion level control

def encrypteMessage(message):
	newMessage = ""
	if verify:
		newMessage = encrypteAffineMessage(message)
		newMessage = encryptVigenerWord(newMessage)
		newMessage = addString(newMessage)
		return newMessage
	else:
		return "Sorry your message can't be encrypted"
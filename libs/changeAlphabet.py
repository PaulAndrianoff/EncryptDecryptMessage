from libs.settings import alphabetUrl, defaultAlphabetUrl, defaultAppHeader
from libs.verification import alphaLen, alphaContent, getAlphabet
from libs.sysCommand import clear, pause

def changeCurentAlphabet():
	getAlphabet()

def setNewAlphabet(add=False):
	if add == False:
		alphabetFile = open(alphabetUrl, 'w')
		newAlphabet = input('''Write all characters you want in your alphabet (Special char not yet implement):\n''')
	else:
		alphabetFile = open(alphabetUrl, 'a+')
		newAlphabet = input('''Write all characters you want to add in your alphabet (Special char not yet implement):\n''')
	alphabetFile.write(newAlphabet)
	alphabetFile.close()
	changeCurentAlphabet()

def setDefaultAlphabet():
	alphabetFile = open(alphabetUrl, 'r').readlines()[0]
	defaultAlphabet = open(defaultAlphabetUrl, 'w')
	defaultAlphabet.write(alphabetFile)
	defaultAlphabet.close()
	print('Set new default alphabet.')

def restoreDefaultAlphabet():
	defaultAlphabet = open(defaultAlphabetUrl, 'r').readlines()[0]
	alphabetFile = open(alphabetUrl, 'w')
	alphabetFile.write(defaultAlphabet)
	alphabetFile.close()
	print('Restore default alphabet.')
	changeCurentAlphabet()

def changeAlphabet():
	while True:
		clear()
		print(defaultAppHeader)
		print('\n Your current alphabet is:\n' + getAlphabet() + '\n')
		choice = input('''
1°) Change your alphabet
2°) add characters to your alphabet
3°) Set your current alphabet as your default one
4°) Restore your default alphabet
[else to return] Please enter your choice: ''')

		if choice == '1':
			setNewAlphabet()
		elif choice == '2':
			setNewAlphabet(True)
		elif choice == '3':
			setDefaultAlphabet()
		elif choice == '4':
			restoreDefaultAlphabet()
		else:
			break
		pause()
		
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.'!?123456789
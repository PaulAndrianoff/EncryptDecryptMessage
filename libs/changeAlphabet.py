from libs.settings import alphabetUrl, defaultAlphabetUrl, defaultAppHeader
from libs.verification import alphaLen, alphaContent
from libs.sysCommand import clear

def setNewAlphabet():
	newAlphabet = input('Write all characters you want in you alphabet (Special char not yet implement):\n')
	alphabetFile = open(alphabetUrl, 'w')
	alphabetFile.write(newAlphabet)
	alphabetFile.close()

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

def changeAlphabet():
	print('\n Your current alphabet is:\n' + alphaContent + '\n')
	while True:
		clear()
		print(defaultAppHeader)
		choice = input('''
1°) Change your alphabet
2°) Set your current alphabet as your default one
3°) Restore your default alphabet
[else to return] Please enter your choice: ''')

		if choice == '1':
			setNewAlphabet()
			changeAlphabet()
		elif choice == '2':
			setDefaultAlphabet()
		elif choice == '3':
			restoreDefaultAlphabet()
		else:
			break
		
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.'!?123456789
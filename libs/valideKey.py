from libs.settings import keysUrl, defaultKeystUrl, defaultAppHeader
from libs.verification import myKeys, verify, getAllKey, alphaLen, getVerify
from libs.sysCommand import clear, pause
from libs.mathFunction import coprime

def setNewKey():
	global verify
	# print('\nYour keys: a=' + str(myKeys[0]) + ' - b=' + str(myKeys[1]) + '\n')
	keysFile = open(keysUrl, 'w')
	while True:
		try:
			aKey = int(input("\nIn (ax + b)mod m, a = "))
			bkey = int(input("\nand b = "))
			wordKey = input("\nYour key word or phrase = ")

			keysFile.write(str(aKey) + "\n" + str(bkey) + "\n" + wordKey)
			keysFile.close()
			break
		except Exception as e:
			print (str(e))
	

def valideKey():
	global verify
	while True:
		setNewKey()
		getAllKey()
		if getVerify():
			print('You set new key.')
			break

def setDefaultAlphabet():
	keysFile = open(keysUrl, "r").readlines()
	defaultKeysFile = open(defaultKeystUrl, "w")
	defaultKeysFile.write(keysFile[0] + keysFile[1])
	defaultKeysFile.close()
	print('You have set a=' + str(myKeys[0]) + ' - b=' + str(myKeys[1]) + ' has your default key')

def restoreDefaultKey():
	defaultKeysFile = open(defaultKeystUrl, "r").readlines()
	keysFile = open(keysUrl, "w")
	keysFile.write(defaultKeysFile[0] + defaultKeysFile[1])
	keysFile.close()
	print('You have restore your default key has a=' + defaultKeysFile[0] + ' - b=' + defaultKeysFile[1])

def changeKey():
	while True:
		clear()
		print(defaultAppHeader)
		try:
			tempKey = getAllKey()
			print('\nYour current keys are :\na=' + str(tempKey[0]) + ' - b=' + str(tempKey[1]) + '\nkeyWord=' + tempKey[2])
		except Exception as e:
			print("Your key are not valide please change them " + str(e))
		choice = input('''
1°) Change your keys
2°) Set your current keys as your default one
3°) Restore your default keys
[else to return] Please enter your choice: ''')

		if choice == '1':
			valideKey()
		elif choice == '2':
			setDefaultAlphabet()
		elif choice == '3':
			restoreDefaultKey()
		else:
			break
		pause()
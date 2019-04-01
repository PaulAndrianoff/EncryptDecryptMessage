from libs.settings import keysUrl, defaultKeystUrl, defaultAppHeader
from libs.verification import myKeys, verify
from libs.sysCommand import clear

def setNewKey():
	print('\nYour keys: a=' + str(myKeys[0]) + ' - b=' + str(myKeys[1]) + '\n')
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
	while True:
		setNewKey()
		if verify:
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
	print('\nYour current keys are a=' + str(myKeys[0]) + ' - b=' + str(myKeys[1]) + ' - keyWord=' + myKeys[2])
	while True:
		clear()
		print(defaultAppHeader)
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
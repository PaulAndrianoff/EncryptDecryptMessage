# Python Module
import os
from datetime import date

# Inner Function
from libs.settings import encryptFolder, decryptFolder
from libs.encryption import encrypteMessage
from libs.decryption import decrypteMessage
from libs.valideKey import valideKey, changeKey
from libs.changeAlphabet import changeAlphabet

clear = lambda: os.system('cls')

def main():
	clear()
	print('''||--------------------------------------------------||
||	  Made by Paul Andrianoff - v.1.0           ||
||--------------------------------------------------||
||	 Encryption and decryption affine           ||
||__________________________________________________||
	''')
	currentMessage = ''
	while True:
		choice = input(
'''
-- Encryption and decryption affine --

1°) Encypte a file
2°) Decrypte a file
3°) Change your keys
4°) Change your alphabet
[else to exit] Please enter your choice: ''')

		if choice == '1':
			try:
				tempFile = open(input('Enter file path of your message: ').replace('\\', '/').replace('"', ''), 'r').readlines()
				myMessage = ""

				for line in tempFile:
					myMessage = myMessage + line
				
				currentMessage = encrypteMessage(myMessage)

				filename = input("Please, name your encrypted file: ")
				today = date.today()

				encryptedFile = open(encryptFolder + str(today) + "_" + filename + ".txt", 'w')
				encryptedFile.write(currentMessage)
				encryptedFile.close()

				print('\nDone.\nYour encrypted message is now in ' + encryptFolder + ' directory.\n')
			except Exception as e:
				print("Sorry. Can't read your file. Please import another one." + str(e))
		
		elif choice == '2':
			if currentMessage == '' or True:
				try:
					tempFile = open(input('Enter file path of your message: ').replace('\\', '/').replace('"', ''), 'r').readlines()
					myMessage = ""

					for line in tempFile:
						myMessage = myMessage + line
					currentMessage = decrypteMessage(myMessage)

					filename = input("Please, name your encrypted file: ")
					today = date.today()

					decryptedFile = open(decryptFolder + str(today) + "_" + filename + ".txt", 'w')
					decryptedFile.write(currentMessage)
					decryptedFile.close()

					print('\nDone.\nYour decrypted message is now in ' + decryptFolder + ' directory.\n')
				except:
					print("Sorry. Can't read your file. Please import another one")
			else:
				currentMessage_new = decrypteMessage(currentMessage)
				print('\nYour original message is now: ' + currentMessage_new)
		elif choice == '3':
			changeKey()
			exit()
		elif choice == '4':
			changeAlphabet()
			exit()
		else:
			break

if __name__ == '__main__':
    main()
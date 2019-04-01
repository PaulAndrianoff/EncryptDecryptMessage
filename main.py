# Inner Function
from libs.settings import encryptFolder, decryptFolder, defaultAppHeader
from libs.sysCommand import clear, pause
from libs.encryption import encrypteMessage
from libs.decryption import decrypteMessage
from libs.valideKey import valideKey, changeKey
from libs.changeAlphabet import changeAlphabet
from libs.fileFunction import openFile, saveFile

def main():
	clear()
	print(defaultAppHeader)
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
			clear()
			myMessage = openFile()
							
			currentMessage = encrypteMessage(myMessage)
			saveFile(currentMessage, encryptFolder)

			print('\nDone.\nYour encrypted message is now in ' + encryptFolder + ' directory.\n')
		except Exception as e:
			print("Sorry. Can't read your file. Please import another one." + str(e))

		pause()

	elif choice == '2':
		try:
			clear()
			myMessage = openFile()

			currentMessage = decrypteMessage(myMessage)
			saveFile(currentMessage, decryptFolder)

			print('\nDone.\nYour decrypted message is now in ' + decryptFolder + ' directory.\n')
		except Exception as e:
			print("Sorry. Can't read your file. Please import another one." + str(e))

		pause()

	elif choice == '3':
		changeKey()
	elif choice == '4':
		changeAlphabet()
	else:
		exit()
	main()
		

if __name__ == '__main__':
    main()
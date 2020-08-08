# Python Module
import datetime
from tkinter import filedialog
import glob
import os

# Inner Function
from libs.settings import encryptFolder, decryptFolder

def openFile(path="/Document"):
	pathFile = filedialog.askopenfilename(initialdir = path,title = "Choose a file",filetypes = (("text files","*.txt"),("all files","*.*")))

	tempFile = open(pathFile.replace('\\', '/').replace('"', ''), 'r').readlines()
	myMessage = ""

	for line in tempFile:
		myMessage = myMessage + line
		
	return myMessage

def saveFile(currentMessage, path, name):
	# filename = input("Please, name your encrypted file: ")
	filename = name
	# now = datetime.datetime.now()
	# print(now.strftime("%Y-%m-%d_%H-%M-%s"))
	# today = str(now).replace(" ", "_").replace(":", "-")

	encryptedFile = open(path + filename + ".txt", 'w')
	encryptedFile.write(currentMessage)
	encryptedFile.close()

def deleteAllFile(path):
	# print(str(path) + "*.txt")
	filelist=glob.glob(path + "*.txt")
	for file in filelist:
		os.remove(file)
	print("All files in " + path + " are deleted")
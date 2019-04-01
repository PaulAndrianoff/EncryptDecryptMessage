# Python Module
import datetime
from tkinter import filedialog
from tkinter import *

# Inner Function
from libs.settings import encryptFolder, decryptFolder

def openFile():
	pathFile = filedialog.askopenfilename(initialdir = "/Document",title = "Choose a file",filetypes = (("text files","*.txt"),("all files","*.*")))

	tempFile = open(pathFile.replace('\\', '/').replace('"', ''), 'r').readlines()
	myMessage = ""

	for line in tempFile:
		myMessage = myMessage + line
		
	return myMessage

def saveFile(currentMessage, path):
	filename = input("Please, name your encrypted file: ")
	today = str(datetime.datetime.now()).replace(" ", "_").replace(":", "-")

	encryptedFile = open(path + str(today) + "_" + filename + ".txt", 'w')
	encryptedFile.write(currentMessage)
	encryptedFile.close()
# Python Module
from datetime import date
from tkinter import filedialog
from tkinter import *

# Inner Function
from libs.settings import encryptFolder, decryptFolder

def openFile():
	# root = Tk()
	pathFile = filedialog.askopenfilename(initialdir = "/Document",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))

	tempFile = open(pathFile.replace('\\', '/').replace('"', ''), 'r').readlines()
	myMessage = ""

	for line in tempFile:
		myMessage = myMessage + line
		
	return myMessage

def saveFile(currentMessage, path):
	# root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	filename = input("Please, name your encrypted file: ")
	today = date.today()

	encryptedFile = open(path + str(today) + "_" + filename + ".txt", 'w')
	encryptedFile.write(currentMessage)
	encryptedFile.close()
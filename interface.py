from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.ttk import *
from tkinter import ttk
from tkinter.filedialog import *
from libs.encryption import encrypteMessage
from libs.decryption import decrypteMessage
from libs.fileFunction import openFile, saveFile, deleteAllFile
from libs.settings import encryptFolder, decryptFolder, defaultAppHeader

window = Tk()
window.title("EncryptDecrypt")
window.geometry('400x350')

tab_control = ttk.Notebook(window)
mainAction = ttk.Frame(tab_control)
settings = ttk.Frame(tab_control)
tab_control.add(mainAction, text='Main Action')
tab_control.add(settings, text='Settings')
tab_control.pack(expand=1, fill='both')

# Tab1
main_title = Label(mainAction, text="MainAction", font=('Arial', 20))
status = Label(mainAction, text="encrypte mode")

mode = Combobox(mainAction)
mode['values'] = ('encrypt', 'decrypt')
mode.current(0)

txt = scrolledtext.ScrolledText(mainAction, width=60, height=10)
selecteFile = Button(mainAction, text="open file")
saveFileTo = Button(mainAction, text="save message")
start = Button(mainAction, text="Start")

main_title.grid(column=1, row=0, sticky='nw')
status.grid(column=2, row=1)
mode.grid(column=1, row=1)
txt.grid(column=1, row=2, columnspan=8)
selecteFile.grid(column=1, row=3, sticky='nw', columnspan=2)
saveFileTo.grid(column=2, row=3, sticky='nw', columnspan=2)
start.grid(column=3, row=3, sticky='ne', columnspan=2)

# Tab2
set_title = Label(settings, text="Settings", font=('Arial', 20))
set_title.grid(column=1, row=0)

def changeMode(ev):
    newMessaeg = mode.get() + " mode"
    status.configure(text=newMessaeg)

def startingMode():
    message = txt.get('1.0', 'end-1c')
    currentMessage = ''
    if 'encrypt' in mode.get():
        currentMessage = encrypteMessage(message)
    else:
        currentMessage = decrypteMessage(message)
    
    txt.delete(1.0, END)
    txt.insert(INSERT, currentMessage)
    messagebox.showinfo('Message status', 'Your message was ' + mode.get(), icon='info', parent=window)

def readNewFile():
    txt.insert(INSERT, openFile())

def saveNewFile():
    name = simpledialog.askstring('Filename', 'enter filename', parent=window)
    saveFile(txt.get('1.0', 'end-1c'), encryptFolder, name)
    messagebox.showinfo('Message status', 'Your message was saved', icon='info', parent=window)

mode.bind("<<ComboboxSelected>>", changeMode)
start.configure(command=startingMode)
selecteFile.configure(command=readNewFile)
saveFileTo.configure(command=saveNewFile)

window.mainloop()
import os
import platform

osName = platform.system()

if osName == 'Windows':
	clear = lambda: os.system('cls')
	pause = lambda: os.system('pause')
else:
	clear = lambda: os.system('clear')
	pause = lambda: os.system('pause')


# print(osName)
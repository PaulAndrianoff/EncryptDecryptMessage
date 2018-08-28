import os
import platform

osName = platform.system()

if osName == 'Windows':
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')


# print(osName)
import pyautogui
from time import sleep
from os import system

while True:
	try:
		system('clear')
		x, y = pyautogui.position()
		print('Mouse Position')
		print(f'x: {x}')
		print(f'y: {y}')
		print('Press Ctrl + C to quit.')
		sleep(.8)
	except KeyboardInterrupt as e:
		break
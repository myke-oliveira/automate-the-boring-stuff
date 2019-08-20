#! /home/myke/anaconda3/bin/python

# Write a program that walks through a folder tree and searches for files with
# a certain file extension (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder.
import os
import shutil
from sys import exit

origin_folder = input('Type de Origin Folder: ')
destiny_folder = input('Type the Destiny Folder: ')
extention = input('Type the extention: ')

if not os.path.exists(destiny_folder):
	os.mkdir(destiny_folder)

for foldername, subfolders, filenames in os.walk(origin_folder):
	for filename in filenames:
		if filename.endswith(extention):
			try:
				shutil.copy(os.path.join(foldername, filename), destiny_folder)
			except Exception as e:
				print('ERROR:')
				print(format(e))
				op = input('Do you wish to continue the copy? (Y/n) ')
				if op is 'n':
					exit()


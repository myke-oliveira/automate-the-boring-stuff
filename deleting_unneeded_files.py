#! /home/myke/anaconda3/bin/python

import os
import send2trash

folder = '/home/myke/'
extention = '.tmp'

for foldername, subfoldernames, filenames in os.walk(folder):
	for filename in filenames:
		if filename.endswith(extention):
			print(filename)
			send2trash.send2trash(os.path.join(foldername, filename))
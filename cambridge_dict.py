#! /home/myke/anaconda3/bin/python

import webbrowser, pyperclip
from sys import argv

if len(argv) > 1:
	words = argv[1:]
else:
	words = [pyperclip.paste()]

for word in words:
	webbrowser.open(f'https://dictionary.cambridge.org/us/dictionary/english-portuguese/{word}')

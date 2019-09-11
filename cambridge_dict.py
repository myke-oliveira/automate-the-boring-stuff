import webbrowser
from sys import argv

words = argv.copy()
words.remove('cambridge_dict.py')

for word in words:
	webbrowser.open(f'https://dictionary.cambridge.org/us/dictionary/english-portuguese/{word}')

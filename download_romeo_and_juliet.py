import requests, os

url = 'http://www.gutenberg.org/cache/epub/1112/pg1112.txt'
res = requests.get(url)
try:
	res.raise_for_status()
except Exception as e:
	print(f'There was a problem: {e}')
	os.exit(1)

with open('Romeo and Juliet.txt', 'wb') as playFile:
	for chunk in res.iter_content(100000):
		playFile.write(chunk)

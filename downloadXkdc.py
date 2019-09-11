import requests, sys, bs4, os, shutil

urlbase = 'https://xkcd.com'
url = 'https://xkcd.com/1/'

print('Creating directory for pictures...')
os.makedirs('xkcdimages', exist_ok=True)

while not url.endswith('#'):
	print(f'Accessing {url}')
	res = requests.get(url)

	try:
		res.raise_for_status()
	except Exception as e:
		print(f'Error Occured: {e}')
		sys.exit(1)

	print('Parsing...')
	soup = bs4.BeautifulSoup(res.text, 'lxml')

	nexturl = urlbase + soup.select('#middleContainer > ul:nth-child(2) > li:nth-child(4) > a')[0]['href']

	urlimage = 'https:' + soup.select('#comic img')[0]['src']
	print(f'Image url {urlimage}')
	res = requests.get(urlimage)

	try:
		res.raise_for_status()
	except Exception as e:
		print(f'Error Occured: {e}')
		sys.exit(1)
	
	with open(os.path.join('xkcdimages', os.path.split(urlimage)[1]), 'wb') as imgfile:
		for chunk in res.iter_content(1000000):
			imgfile.write(chunk)
	
	url = nexturl

import requests, bs4, sys, os

url = 'https://www.vidadeprogramador.com.br/'

directoryname = 'vidadeprogramador'

os.makedirs(directoryname, exist_ok=True)

while True:
	print(f'Page URL: {url}')
	res = requests.get(url)
	try:
		res.raise_for_status()
	except Exception as e:
		print(f'An error has occurred: {e}')
		sys.exit(1)

	soup = bs4.BeautifulSoup(res.text, 'lxml')

	for tag in soup.select('div.tirinha > a'):
		imageurl = tag.get('href')
		print(f'Image URL: {imageurl}')
		imagefilename = os.path.basename(imageurl)
		resimage = requests.get(imageurl)
		try:
			resimage.raise_for_status()
		except Exception as e:
			print(f'An error has occurred: {e}')
		with open(os.path.join(directoryname, imagefilename), 'wb') as imagefile:
			for chunk in resimage.iter_content(100000):
				imagefile.write(chunk)
	try:
		url = soup.select('.prev > a')[0].get('href')
	except Exception as e:
		print(e)	
		break

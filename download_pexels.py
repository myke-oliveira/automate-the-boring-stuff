#! /home/myke/anaconda3/bin/python

import requests, bs4, sys, os

term = input('Type term for searching: ')
directory = os.path.join('pexels', term)
os.makedirs(directory, exist_ok=True)
print(f'Directory {directory} created.')
url = f'https://www.pexels.com/search/{term}/'
print(f'Acessing {url}...')
res = requests.get(url)
try:
	res.raise_for_status()
except Exception as e:
	print(f'An error has occured: {e}')
	sys.exit(1)
print('SUCESS')

soup = bs4.BeautifulSoup(res.text, 'lxml')
print('Starting...')
imgtags = soup.find_all('img', class_='photo-item__img')
for imgtag in imgtags:
 	imageurl = imgtag['src']
 	print(f'Downloading {imageurl}...')
 	imageres = requests.get(imageurl)
 	filename = os.path.basename(imageurl)
 	print(f'Saving {filename}...')
 	for chunk in imageres.iter_content(100000):
 		with open(os.path.join(directory, filename), 'wb') as imagefile:
 			tam = imagefile.write(chunk)
 			print(f'{tam} bytes...')
 	print('Saved.')

import os, zipfile

source_folder = '/home/myke/'
extention = '.pdf'

# dest = input('Enter the name of the file: ')
dest = 'meuspdf.zip'

print(f'Creating {dest} file.')
with zipfile.ZipFile(dest, 'w') as myZipFile:
	for foldername, subfoldernames, filenames in os.walk(source_folder):
		for filename in filenames:
			if filename.endswith('.pdf'):
				print('Directory {}: File {}'.format(foldername, filename))
				myZipFile.write(os.path.join(foldername, filename))



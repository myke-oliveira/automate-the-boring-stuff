import os, shutil

directory = input('Enter directory: ')

for dirpath, dirnames, filenames in os.walk(directory):
	for filename in filenames:
		org = os.path.join(dirpath, filename)
		des = org.split('?')[0]
		print(f'Origem: {org}')
		print(f'Dest: {des}')
		shutil.move(org, des)

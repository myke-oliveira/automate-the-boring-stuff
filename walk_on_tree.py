from os import walk

for folder_name, subfolders, filenames in walk('/home'):
	print(f'The current folder is {folder_name}.')

	for subfolder in subfolders:
		print(f'SUBFOLDER OF {folder_name}: {subfolder}')

	for filename in filenames:
		print(f'FILE INSIDE {folder_name}: {filename}')

print()
import re, os, sys

try:
	if sys.argv[1] == '--directory' and os.path.isdir(sys.argv[2]):
		os.chdir(sys.argv[2])
except IndexError:
	pass

regex_email     = re.compile(r'(\w+@\w+(\.\w+)*)')
regex_phone_num = re.compile(r'\(\d{2,3}\)\s?\d{4,5}-\d{4}')
for file_path in [fp for fp in os.listdir() if fp.endswith('.txt')]:
	print(f'{file_path:-^80}')
	with open(file_path, 'r') as file:
		text = file.read()
	print(regex_email.findall(text))
	print(regex_phone_num.findall(text))

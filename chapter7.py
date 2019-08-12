import re

def is_strong_password(password):
	if len(password) < 8:
		return False
	regex_lowercase = re.compile(r'[a-z]')
	regex_uppercase = re.compile(r'[A-Z]')
	regex_digit = re.compile(r'\d')
	if regex_uppercase.search(password) == None:
		return False
	if regex_lowercase.search(password) == None:
		return False
	if regex_digit.search(password) == None:
		return False
	return True

def myke_s_strip(word):
	regex = re.compile(r'^\s*(.*)\s*$')
	match = regex.search(word)
	return match.group(1)

while True:
	word = input('Enter a password: ')
	print(is_strong_password(word))
	print(myke_s_strip(word))

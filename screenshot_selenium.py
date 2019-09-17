from selenium import webdriver

with webdriver.Chrome() as chrome:
	chrome.get('https://www.google.com.br')
	chrome.save_screenshot('google.png')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
with webdriver.Chrome(options=options) as chrome:
	chrome.get('https://play2048.co/')
	html = chrome.find_element_by_tag_name('html')
	while True:
		html.send_keys(Keys.UP)
		html.send_keys(Keys.LEFT)
		html.send_keys(Keys.DOWN)
		html.send_keys(Keys.RIGHT)

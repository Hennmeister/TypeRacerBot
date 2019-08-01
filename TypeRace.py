from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time

def startup():
	driver = webdriver.Chrome()
	driver.get("https://play.typeracer.com/")
	driver.find_element_by_link_text('Enter a typing race').click()
	inputTxt = getText(driver)
	#print(getText(driver))
	try:
		countdown = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.CLASS_NAME, "lightLabel")))
	except TimeoutException:
		print "failed to find lightLabel"

	try:
		WebDriverWait(driver, 15).until(EC.staleness_of(countdown))
		print "done"
		sendText(driver, inputTxt)
	except TimeoutException:
		print "failed"

def getText(driver):
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	#for span in soup.find_all('span'):
		#spanStr = span.encode("utf-8")
	spanList = soup.find_all('span')
	for i in range(len(spanList)):
		spanStr = spanList[i].text
		if spanStr.endswith('.'):
			keysStr = spanList[i-2].text +  spanList[i-1].text + spanList[i].text
			print("keysStr: " + keysStr)
	return(keysStr)

def sendText(driver, inputTxt):
	print("send text")
	actions = ActionChains(driver)
	for c in inputTxt:
		actions.send_keys(c)
		time.sleep(1)
		actions.perform()

def main():
	startup()

if __name__ == "__main__":
	main()
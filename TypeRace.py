from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://play.typeracer.com/")

delay = 10 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'gwt-Anchor')))
    print "Found"
except TimeoutException:
    print "Timed out"

driver.find_element_by_link_text('Enter a typing race').click()

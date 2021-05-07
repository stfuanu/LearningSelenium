import json
import sys
import time

from os import walk
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9050)
profile.set_preference("network.proxy.socks_version", 5)
profile.update_preferences()

options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_profile= profile , options=options , executable_path='/usr/bin/geckodriver')
driver.implicitly_wait(0.5)
driver.get('https://www.dnsleaktest.com')
print(driver.title)
l=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/p[1]").text
print("My IP is : " + l)
driver.quit()

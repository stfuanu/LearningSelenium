import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium import webdriver
path = r"${WEBDRIVER_PATH}"

driver = webdriver.Chrome(path)
driver.get("https://hackerone.com/users/sign_in")

# Function to verify that Web Page opened using ( WebDriverWait & expected_conditions )
# "By" matching [XPATH,ID,NAME,CLASS_NAME] etc..

def verify(by):
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(by)
        )
    except:
        driver.quit()


verify((By.NAME, "commit"))

driver.find_element_by_xpath("//*[@id='sign_in_email']").send_keys("${EMAIL}")
driver.find_element_by_xpath("//*[@id='sign_in_password']").send_keys("${PASSWORD}")
driver.find_element_by_id("user_remember_me").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/div/div/div/div[2]/div/div/div[4]/button").click()

verify((By.XPATH, "/html/body/div[2]/div/div[1]/span/div/div/div[2]/ul/li[3]/a"))

driver.get("https://hackerone.com/bugs")
# An Authenticated page Opened .

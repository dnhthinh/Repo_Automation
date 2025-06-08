from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.expected_conditions import title_is

#config browser
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.set_window_size(1920,1080)

#Handling elemnts
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#Searching Admin page
driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("Admin")
driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item']").click()
#Adding user
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
drop_down = driver.find_element(By.CLASS_NAME,"oxd-select-text")
drop_down.click()
#option = driver.find_element()
time.sleep(4)
current_url = driver.current_url

print(current_url)

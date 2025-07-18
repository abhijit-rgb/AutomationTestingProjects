import time

from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome()

webdriver.get("https://rahulshettyacademy.com/client/")

webdriver.maximize_window()

webdriver.find_element(By.LINK_TEXT, 'Register here').click()

webdriver.find_element(By.XPATH, '//form/div[1]/div[1]//input').send_keys('ABHIJIT')

webdriver.find_element(By.XPATH, '//form/div[1]/div[2]/div/input').send_keys('MESHRAM')

webdriver.find_element(By.XPATH, '//form/div[2]/div[1]/input').send_keys('demo@123.com')

webdriver.find_element(By.XPATH, '//form/div[2]/div[2]/input').send_keys('1234567890')

webdriver.find_element(By.XPATH, '//form/div[3]/div[1]/select').send_keys('Engineer')

webdriver.find_element(By.XPATH, '//form/div[3]/div[2]/label[2]').click()

webdriver.find_element(By.XPATH, '//form/div[4]/div[1]/input').send_keys('Demo@123')

webdriver.find_element(By.XPATH, '//form/div[4]/div[2]/input').send_keys('Demo@123')

webdriver.find_element(By.XPATH, '//form/div[5]/div[1]').click()

webdriver.find_element(By.XPATH, '//form/input').click()





















time.sleep(10)
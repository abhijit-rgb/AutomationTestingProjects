from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome()

webdriver.get('https://rahulshettyacademy.com/angularpractice/')

webdriver.find_element(By.NAME, 'name').send_keys('ABC')

webdriver.find_element(By.NAME,'email').send_keys('ABC@123.com')

webdriver.find_element(By.ID,'exampleInputPassword1').send_keys('DemoPassword')

webdriver.find_element(By.ID,'exampleCheck1').click()

webdriver.find_element(By.ID,'exampleFormControlSelect1').send_keys('Male')

webdriver.find_element(By.ID,'inlineRadio2').click()

webdriver.find_element(By.NAME,'bday').send_keys('09-04-1998')

webdriver.find_element(By.CLASS_NAME,'btn-success').click()

message = webdriver.find_element(By.CLASS_NAME, 'alert-success').text

print(message)

assert "Success" in message

sleep(10)




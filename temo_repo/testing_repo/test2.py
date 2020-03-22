from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()




def login_func(driver , url):
	driver.get(url)
	user = driver.find_element_by_id('username')
	user.send_keys('admin')
	password =  driver.find_element_by_id('password')
	password.send_keys('admin')
	path = '/html/body/div[2]/div[1]/div/div[2]/div[5]'
	time.sleep(2)
	cont =  driver.find_element_by_xpath(path)
	cont.click()
	#driver.quit()


url = 'http://192.168.0.14/doc/page/login.asp?_1584179772788'
login_func(driver, url)


link = url.split('login.asp')[0]  + 'preview.asp'
print(link)









































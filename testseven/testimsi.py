import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import pandas as pd

store_names = [] # 지점명
addrs = [] # 주소명
office_hours = [] # 영업시간
atms = [] # atm 유무
medicines = [] # 약 유무
breads = [] # 빵 유무
deliveries = [] # 택배 유무

# chromedriver 위치 지정

driver = webdriver.Chrome('C:/Users/i9i91/AppData/Local/Programs/Python/Python37/chromedriver')
driver.maximize_window()
# 웹페이지 접속
driver.get('http://www.7-eleven.co.kr/')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="header"]/div/div/div[1]/a[1]').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="storeLaySido"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="storeLaySido"]/option[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="storeLayGu"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="storeLayGu"]/option[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="storeButton1"]').click()
time.sleep(1)


sus = 0
imsi_sus = driver.find_elements_by_css_selector('#storeForm > div:nth-child(4) > div.list_stroe > ul > li')
for imsi_su in imsi_sus:
    sus = sus + 1
print(sus)

sidosus = 0
sidos = driver.find_elements_by_css_selector('#storeLayGu > option')
for sido in sidos:
    print(sido)
    sidosus = sidosus + 1
print(sidosus)


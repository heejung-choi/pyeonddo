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
for q in range(2,15):    
    driver.find_element_by_xpath('//*[@id="storeLaySido"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="storeLaySido"]/option[18]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="storeLayGu"]').click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='storeLayGu']/option["+str(q)+"]").click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="storeButton1"]').click()
    time.sleep(1)

    boolatm = 'False'
    boolmed = 'False'
    boolbrad = 'False'
    booldeli = 'False'

    sus = 0
    imsi_sus = driver.find_elements_by_css_selector('#storeForm > div:nth-child(4) > div.list_stroe > ul > li')
    for imsi_su in imsi_sus:
        sus = sus + 1
    print(sus)
    for i in range(1,sus):
        imsi_stores = driver.find_elements_by_xpath("//*[@id='storeForm']/div[1]/div[2]/ul/li["+str(i)+"]/a/span[1]")
        imsi_addrs = driver.find_elements_by_xpath("//*[@id='storeForm']/div[1]/div[2]/ul/li["+str(i)+"]/a/span[2]")
        imsi_office_hours = driver.find_elements_by_xpath("//*[@id='storeForm']/div[1]/div[2]/ul/li["+str(i)+"]/a/span[4]")
        for imsi_store in imsi_stores:
            store_names.append(imsi_store.text)

        for imsi_addr in imsi_addrs:
            addrs.append(imsi_addr.text)
        
        for imsi_office_hour in imsi_office_hours:
            office_hours.append(imsi_office_hour.text)

            for j in range(1,13):
                imgs = driver.find_elements_by_xpath("//*[@id='storeForm']/div[1]/div[2]/ul/li["+str(i)+"]/a/span[1]/img["+str(j)+"]")
                for img in imgs:
                    alttext = img.get_attribute('alt')
                    print(alttext)
                    if alttext == 'ATM':
                        boolatm = 'True'                
                    elif alttext == '의약품':
                        boolmed = 'True'
                    elif alttext == '베이커리':
                        boolbrad = 'True'
                    elif alttext == '무인택배접수':
                        booldeli = 'True'
                    else:
                        pass

        atms.append(boolatm)
        medicines.append(boolmed)
        breads.append(boolbrad)
        deliveries.append(booldeli)

print(store_names)
print(addrs)
print(office_hours)
print(atms)
print(medicines)
print(breads)
print(deliveries)

replys = list(zip(store_names, addrs, office_hours, atms, medicines, breads, deliveries))
driver.quit()

col = ['지점명', '주소', '영업시간', 'ATM', '의약품','베이커리','배달']
import pandas as pd
data_frame = pd.DataFrame(replys, columns=col)
data_frame.to_csv('C:/Users/i9i91/OneDrive/바탕 화면/충청북도.csv',encoding='utf-8-sig')

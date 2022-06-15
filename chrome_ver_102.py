import time
import datetime
from selenium import webdriver

#webサイト
chrome = webdriver.Chrome(executable_path = 'C:/Users/利光/Desktop/プログラム/python/chromedriver.exe')
chrome.get("https://www.arealme.com/click-speed-test/ja/")

time.sleep(1)
chrome.find_element_by_id('start').click()

time.sleep(1)
chrome.find_element_by_id('clickarena').click()
min10 = datetime.datetime.now() + datetime.timedelta(seconds = 10)

#10秒間連打
while datetime.datetime.now() <= min10:
    chrome.find_element_by_id('clickarena').click()
    
#3秒待って閉じる    
time.sleep(3)
chrome.quit()
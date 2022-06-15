import time
import datetime
from selenium import webdriver

chrome = webdriver.Chrome(executable_path = 'C:/Users/利光/Desktop/プログラム/python/chromedriver.exe')
chrome.get("https://www.arealme.com/click-speed-test/ja/")

time.sleep(1)
chrome.find_element_by_id('start').click()

time.sleep(1)
chrome.find_element_by_id('clickarena').click()
min10 = datetime.datetime.now() + datetime.timedelta(seconds = 10)

while datetime.datetime.now() <= min10:
    chrome.find_element_by_id('clickarena').click()
        
time.sleep(3)
chrome.quit()



#<button class="progress-button pure-button pure-button-primary" id="start"><span class="content" style="opacity: 1;">測定スタート</span><span class="progress"><span id="progress-inner" style="width: 100%;"></span></span></button>
#<button class="btn btn-default" id="clickarena"><b>出来るだけ早く緑色をタップ・クリックしてください。</b></button>
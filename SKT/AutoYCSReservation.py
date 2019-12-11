from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import datetime
import threading

start = time.time()
#헤더 설정
WINDOW_SIZE = "1920,1080"
options = wd.ChromeOptions()
# options.headless = True
options.add_argument('--disable-gpu')
options.add_argument("--window-size=%s" % WINDOW_SIZE)
# options.add_argument('--start-maximized')

# 사전에 필요한 정보를 로드 => DB, 쉘, 배치 파일에서 인자를 받아서 세팅
main_url = "https://www.ycs.or.kr/yeyak/fmcs/43"
y_id = 'jangjaeda'
y_pw = 'wisl1qaz@wsx'

# 드라이버 로드
driver = wd.Chrome(executable_path='chromedriver.exe', chrome_options=options)
# 차후 -> 옵션 부여하여(프록시, 에이전트 조작, 이미지를 배제)

# 사이트 접속 (get)
driver.get(main_url)
driver.find_element_by_xpath("//*[@id='GNB']/aside/nav/ul/li[1]/a").click()
# driver.find_element_by_xpath("//*[@id='tnb']/ul/li[2]/a").click()

driver.find_element_by_id('id').send_keys(y_id)
driver.find_element_by_id('pw').send_keys(y_pw)
driver.find_element_by_css_selector('.submit').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath("//*[@id='center']/option[4]").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='place']/option[12]").click()
driver.find_element_by_xpath("//*[@id='search']/fieldset/div/div/div/button").click()

driver.save_screenshot('1.png')

print("time :", time.time() - start)

    # 검색 버튼 클릭
    # 잠시 대기 => page가 로드되고 나서 즉각적으로 데이터를 획득하는 행위는 자제

# YCSLogin()

# iTime = datetime.datetime.strptime("2019-12-11 21:15:35", "%Y-%m-%d %H:%M:%S")
# count = 0
#
# def countDown():
#     t = threading.Timer(0.5, countDown)
#     t.start()
#     timeDelta = iTime - datetime.datetime.now()
#     gap = timeDelta.total_seconds()
#     global count
#     if gap <= 0.0 and count == 0:
#         count += 1
#         t.cancel()

# countDown()
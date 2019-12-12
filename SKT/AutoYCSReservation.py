from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#서버시간 동기화, qt필요(예약시간 입력, 타겟 시간 입력, 시간선택)

import time
import datetime
import threading


#헤더 설정
WINDOW_SIZE = "1920,1080"
options = wd.ChromeOptions()
options.headless = True
options.add_argument('--disable-gpu')
options.add_argument("--window-size=%s" % WINDOW_SIZE)
# options.add_argument('--start-maximized')

# 드라이버 로드
driver = wd.Chrome(executable_path='chromedriver.exe', chrome_options=options)

# 사전에 필요한 정보를 로드 => DB, 쉘, 배치 파일에서 인자를 받아서 세팅
main_url = "https://www.ycs.or.kr/yeyak/fmcs/43"
y_id = 'jangjaeda'
y_pw = 'wisl1qaz@wsx'
reserve_date = 'date-20191220'
nPlayer = 2
iTime = datetime.datetime.strptime("2019-12-13 09:29:30", "%Y-%m-%d %H:%M:%S")
count = 0



def YCSLogIn():
    # 사이트 접속 (get)
    global driver
    driver.get(main_url)
    driver.find_element_by_xpath("//*[@id='GNB']/aside/nav/ul/li[1]/a").click()

    # 로그인
    driver.find_element_by_id('id').send_keys(y_id)
    driver.find_element_by_id('pw').send_keys(y_pw)
    driver.find_element_by_css_selector('.submit').click()
    driver.implicitly_wait(1)

    # 대관신청(목동체육관 선택)
    driver.find_element_by_xpath("//*[@id='center']/option[4]").click()
    driver.implicitly_wait(1)

def ExecuteProcess():
    start = time.time()
    print("ExcuteProcess Enter : ", datetime.datetime.now())

    # 대관신청(12번 코트 클릭 후 조회)
    global driver
    driver.find_element_by_xpath("//*[@id='place']/option[12]").click()
    driver.find_element_by_xpath("//*[@id='search']/fieldset/div/div/div/button").click()

    # 시간 선택
    driver.find_element_by_id(reserve_date).click()
    print("ExcuteProcess Choose time : ", datetime.datetime.now())
    driver.find_element_by_xpath("//*[@id='contents']/article/div/div/div[3]/div[2]/div/table/tbody/tr[11]/td[1]/input").click()     #시간변경시 tr[11] 값 변경
    # driver.find_element_by_xpath("//*[@id='contents']/article/div/div/div[3]/div[2]/div/table/tbody/tr[10]/td[1]/input").click()
    driver.find_element_by_css_selector('.action_application').click()
    driver.implicitly_wait(1)


    # 정보 입력 후 예약
    print("ExcuteProcess Last Page : ", datetime.datetime.now())
    driver.find_element_by_id('users').send_keys(nPlayer)
    driver.find_element_by_xpath("//*[@id='agree_use1']").click()
    driver.find_element_by_xpath("//*[@id='writeForm']/fieldset/p[2]/button").click()

    print("ExcuteProcess Leave : ", datetime.datetime.now())
    print("Duration time :", time.time() - start)
    driver.quit()

def countDown():
    t = threading.Timer(0.1, countDown)
    t.start()
    timeDelta = iTime - datetime.datetime.now()
    gap = timeDelta.total_seconds()
    # print(gap)
    global count
    if gap <= 0.0 and count == 0:
        count += 1
        print("Login : ", datetime.datetime.now())
        YCSLogIn()
    elif gap <= -30.0 and count == 1:
        count += 1
        ExecuteProcess()
    elif count == 2:
        t.cancel()

countDown()
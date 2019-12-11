# 인터파크 투어사이트에서 여행지를 입력 후 검색 -> 잠시 후 -> 결과
# 로그인시 PC 웹 사이트에서 처리가 어려울 경우 -> 모바일 로그인 진입
# 모듈 가져오기
# pip install selenium
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 사전에 필요한 정보를 로드 => DB, 쉘, 배치 파일에서 인자를 받아서 세팅
main_url = "http://tour.interpark.com/"
keyword = '로마'

# 드라이버 로드
driver = wd.Chrome(executable_path='chromedriver.exe')
# 차후 -> 옵션 부여하여(프록시, 에이전트 조작, 이미지를 배제)
# 크롤링을 오래돌리면 => 임시파일들이 쌓인다!!

# 사이트 접속 (get)
driver.get(main_url)

# 검색창을 찾아서 검색어 입력
# id : SearchGNBText
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
# 수정할 경우 => 뒤에 내용이 붙어버림 => .clear() 후에 send_keys()


# 검색 버튼 클릭
driver.find_element_by_css_selector('button.search-btn').click()

# 잠시 대기 => page가 로드되고 나서 즉각적으로 데이터를 획득하는 행위는 자제
# 명시적 대기 => 특정 요소가 locate(발견될때까지) 대기
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.ID)        #지정한 한개 요소가 올라오면 웨이트 종료
    )
except Exception as e:
    print("오류발생", e)
finally:
# 암묵적 대기 => DOM이 다 로드 될때까지 대기 하고 먼저 로드되면 바로 진행
# 요소를 찾을 특정 시간 동안 DOM 풀링을 지시 예를 들어 10초 이내라도 발견되면 진행
driver.implicitly_wait(10)
# 절대적 대기 => time.sleep(10) -> 클라우드 페어(디도스 방어 솔루션)

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date


user_ID = 20161591 #input("Your ID : ")
user_PW = 1093415#input("Your PW : ")

driver = webdriver.Chrome(r"C:\Users\r00t0k\Documents\r00t0k\project\chromedriver\chromedriver.exe")


driver.get('https://eclass1.dongseo.ac.kr/')

driver.find_element_by_xpath('//*[@id="header"]/nav/div/div[1]/div[3]/div[2]/a').click()

try:
    driver.find_element_by_id('userid').send_keys(user_ID)
    driver.find_element_by_id('password').send_keys(user_PW)
    driver.find_element_by_id('btnLogin').click()
    driver.find_element_by_id('menu-item-5c6b7f952b16ce0dd83f8882').click()
except:
    print("ID / PW 를 확인하세요. ")



driver.get('https://canvas.dongseo.ac.kr/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


TD = date.today()
#print('Today : ' + TD.year + '년' + TD.month + '월' + TD.day + '일')




while(1):
    print('------동작 목록------')
    
    print('1. 수업 목록 보기')
    print('2. 밀린 동영상 강의 시청')
    print('3. 해야할 과제 출력')

    Select_Num = int(input("동작을 선택하세요(-1 입력시 종료) : "))
    print(Select_Num)

    if Select_Num == -1:
        print('3초 후 종료합니다.')
        time.sleep(3)
        driver.quit()
        break

    elif Select_Num == 1: # 강의 목록 출력
        notices = soup.select('div div div div div a div h2')
        print(notices)
        for lst in notices:
            print(lst.string)

    elif Select_Num == 2: #밀린 동영상 강의 자동 시청
        Clist_Num = len(driver.find_elements_by_class_name('ic-DashboardCard')) # 과목 개수
        for count in range(0, Clist_Num): # 과목개수 만큼 돈다.
            Clist = driver.find_elements_by_class_name('ic-DashboardCard') #ic-DashboardCard
            Clist[count].click()
            try:
                driver.find_element_by_class_name('context_external_tool_3').click() # 수업콘텐츠 입장
            except:
                print('강의가 없는 수업입니다.' + driver.find_element_by_class_name('ellipsible').text) # 수정해야함!!!!!!!!!!!!!!!!!
            try:
                driver.find_element_by_class_name('xncl-btn-unfold-sections xn-common-white-btn').driver.find_element_by_class_name('xn-common-btn-unfold-icon').click()  #펼치기
            except:
                print('이미 펼쳐져 있습니다.')
            try:
                driver.switch_to_frame('tool_content') #tool_content
            except:
                pass
            CL_avi = driver.find_elements_by_css_selector('div.xn-component-item-container.learn.open.attendance')
            print(CL_avi)
            #CL_avi[0].click()
            driver.switch_to.default_content()

            #print(CL_avi) # test
            driver.find_element_by_class_name('ic-icon-svg--dashboard').click() # 돌아가기
            
            

        pass
    elif Select_Num == 3:
        pass
    else:
        print('번호를 잘못 입력하였습니다. 다시 확인해 주세요.')




"""1
search = driver.find_element_by_name('q')
search.send_keys('Test')
search.submit()
time.sleep(2)
"""
#driver.quit()

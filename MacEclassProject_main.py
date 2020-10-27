import time
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date


user_ID = 20161591 #input("Your ID : ")
user_PW = 1093415#input("Your PW : ")

driver = webdriver.Chrome(r"/Users/r00t0k/CD/chromedriver")


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

def playVideo():
    pass

def switchIframe():
    driver.switch_to.frame("tool_content")
    return

def EndswitchIframe():
    driver.switch_to.default_content()
    return

while(1):
    print('------동작 목록------')

    print('1. 수업 목록 보기')
    print('2. 밀린 동영상 강의 시청 (들을 수 있는 수업은 전부 자동 시청합니다.)')
    print('3. 해야할 과제 출력\n\n')

    Select_Num = int(input("동작을 선택하세요(-1 입력시 종료) : "))
    print(Select_Num)

    if Select_Num == -1:
        print('3초 후 종료합니다.')
        time.sleep(3)
        driver.quit()
        break

    elif Select_Num == 1: # 강의 목록 출력
        notices = soup.select('div div div div div a div h2')
        #4print(notices)
        for lst in notices:
            print(lst.string)

    elif Select_Num == 2: #밀린 동영상 강의 자동 시청
        Clist_Num = len(driver.find_elements_by_class_name('ic-DashboardCard')) # 과목 개수
        for count in range(0, Clist_Num): # 과목개수 만큼 돈다.
            Clist = driver.find_elements_by_class_name('ic-DashboardCard') #ic-DashboardCard
            Clist[count].click()
            print("이 수업은 ", driver.find_elements_by_class_name("ellipsible")[1].text, "수업 입니다.")
            try:
                driver.find_element_by_class_name('context_external_tool_3').click()
                switchIframe()

                try:
                    driver.find_element_by_class_name('xn-common-btn-unfold-icon').click()
                    print("강의를 펼쳤습니다.")
                except:
                    print("강의가 이미 펼쳐져 있습니다.")

                # 행동 입력
                EndswitchIframe()
                switchIframe()
                time.sleep(1.5)



                ClassNotTakenA = (driver.find_elements_by_css_selector("div.xnci-description-component-type-icon.learn.unpublished.start.movie")) # 법정교육 같은 수업들 카운트
                ClassNotTakenB = (driver.find_elements_by_css_selector("div.xnci-description-component-type-icon.learn.unpublished.start.everlec")) # 법정교육말고 다른 수업들 카운트
                print("들을수 있는 수업이 ", (len(ClassNotTakenA + ClassNotTakenB)), "개 있습니다.\n")


                ClassNotTakenNameList = ClassNotTakenA + ClassNotTakenB

                for ClassNotTake in ClassNotTakenNameList:
                    ClassNotTake.click()
                '''
                for i in classNameList:
                    print(i.text)
                    i.click()
                classNameList = []
                #print(classNameList)
                '''
                #print(element_count)
                #print("video count: " + len(element_count))


                EndswitchIframe()
                driver.back()

            except:
                print(driver.find_elements_by_class_name('ellipsible')[1].text + ' 수업은 수업 콘텐츠가 없습니다.')
            driver.back()
            #driver.find_element_by_id('global_nav_dashboard_link').click() # 돌아가기(공통된 대쉬보드 값 찾기)


    elif Select_Num == 3:
        pass
    else:
        print('번호를 잘못 입력하였습니다. 다시 확인해 주세요.')




"""1
search = driver.find_element_by_name('q')
search.send_keys('Test')
search.submit()
time.sleep(2)





            iframe = driver.find_elements_by_tag_name('iframe')
            print('현재 페이지에 iframe은',len(iframe) ,'개가 있습니다.')
            driver.switch_to_frame(iframe[-1]) #tool_content

            CL_avi = driver.find_elements_by_class_name('xnslh-section-title')
            print(CL_avi)
            driver.switch_to.default_content()

            #print(CL_avi) # test
"""
#driver.quit()

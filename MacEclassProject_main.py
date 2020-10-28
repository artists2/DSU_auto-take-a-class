import time
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime


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




def switchIframe():
    driver.switch_to.frame("tool_content")
    return

def EndswitchIframe():
    driver.switch_to.default_content()
    return


def PlayVideo():
    print(driver)
    VideoBody = driver.find_elements_by_class_name("xnbc-body")

    print("페이지의 동영상 개수:  " + str(len(VideoBody)))
    return


while(1):
    print(datetime.today())
    print('------동작 목록------')

    print('1. 수업 목록 보기')
    print('2. 밀린 동영상 강의 시청 (들을 수 있는 수업은 전부 자동 시청합니다.)')
    print('3. 해야할 과제 출력\n\n')

    Select_Num = int(input("동작을 선택하세요(-1 입력시 종료) : "))

    if Select_Num == -1:
        print('3초 후 종료합니다.')
        time.sleep(3)
        driver.quit()
        break

    elif Select_Num == 1: # 강의 목록 출력
        notices = soup.select('div div div div div a div h2')
        for lst in notices:
            print(lst.string)
        print("\n\n")

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
               # EndswitchIframe()
               # switchIframe()
                time.sleep(1.5)

                ClassNotTakenList = driver.find_elements_by_css_selector("span.xnci-attendance-status.none")
                print("미수강 수업의 개수 : " + str(len(ClassNotTakenList)))
                for ClassNotTake in ClassNotTakenList:
                    ClassNotTake.click()
                    time.sleep(2)
                    #############위는 정상코드:
                    PlayVideo()
                    print("TEEEEEEEEEEEEEEEEEEEEEEEEEEST")
                    driver.back()
                    time.sleep(5)
                    switchIframe()
                    driver.find_element_by_class_name('xn-common-btn-unfold-icon').click()
                    print("강의를 펼쳤습니다.")
                    time.sleep(3)
                    continue

                EndswitchIframe()
                #driver.back()

            except:
                print(driver.find_elements_by_class_name('ellipsible')[1].text + ' 수업은 수업 콘텐츠가 없습니다.\n')
            driver.back()
            #driver.find_element_by_id('global_nav_dashboard_link').click() # 돌아가기(공통된 대쉬보드 값 찾기)


    elif Select_Num == 3:
        print("\n곧 마감 되는 수업이나 과제를 알려드립니다.")

        driver.find_element_by_xpath("//*[@id='right-side']/div[2]/ul/li[18]/a").click()

        EndClassName = driver.find_elements_by_xpath("//*[@id='right-side']/div[2]/ul/li[*]/a/div/b")
        EndClassSubject = driver.find_elements_by_xpath("//*[@id='right-side']/div[2]/ul/li[*]/a/div/p[1]")
        EndClassTime = driver.find_elements_by_xpath("//*[@id='right-side']/div[2]/ul/li[*]/a/div/p[2]")

        time.sleep(2)

        print("해야할 과제 수: " + str(len(EndClassName)) + "개\n")
        for endclassNum in range(0, len(EndClassName)):
            if EndClassTime[endclassNum].text[0] == 'C':
                continue
            print(EndClassSubject[endclassNum].text + "\n " + EndClassName[endclassNum].text + "\n 제출기간: " + EndClassTime[endclassNum].text  + " 까지 \n\n")
            time.sleep(0.5)
        print("\n\n")
        pass
    else:
        print('번호를 잘못 입력하였습니다. 다시 확인해 주세요.')



#driver.quit()

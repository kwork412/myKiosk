import pyautogui as pg #pyautogui import >> 자동화 기능 구현
import os #os import >> 브라우저 실행
import keyboard

# txt 파일 관리를 위한 class
class ManageFiles:
    
    # 파일 이름 받기
    def __init__(self, filename):
        self.path =  'option\\'+ filename + '.txt'
    
    # 파일 경로 출력
    def file_path(self):
        print(self.path)
    
    # 파일 초기화
    def file_empty(self):
        empty = open(self.path, 'w')
        empty.write('')
        empty.close()
    
    # 파일에 해당 내용 작성하기            
    def file_reWrite(self, contents):
        self.contents = contents
        write_contents = open(self.path, 'w', encoding="UTF-8")
        write_contents.write(self.contents)
        write_contents.close()
    
    # 파일 읽기
    def file_read(self):
        read_contents = open(self.path, 'r', encoding="UTF-8")
        data = read_contents.read()
        return(data)

def os_start(browser, address):
    os.system('start '+ browser + ' ' + address) 
   

#초기설정  0 >> 초기 설정 전
initial = ManageFiles('option')
if ((initial.file_read()) == '0'): #초기 설정을 하지 않은 경우 실행
    
    pg.alert(text = '초기 설정을 시작합니다.', title = 'My Kiosk', button = '확인')
    i = 0
    window_now = 'browser_select'
    while window_now != 'setting_finish':
       
        if window_now == 'browser_select':
            user_browser = pg.confirm(text = '사용할 브라우져를 골라주세요', title = 'My Kiosk - 초기설정', buttons = ['Chrome', 'Edge', 'Whale', '기타'])
    
            if user_browser == 'Chrome':
                user_browser = 'chrome'
        
            elif user_browser == 'Edge':
                user_browser = 'microsoftedge'
        
            elif user_browser == 'Whale':
                user_browser = 'whale'
        
            elif user_browser == '기타':
                user_browser = pg.prompt(text = '사용하실 브라우저를 입력해주세요', title = 'My Kiosk - 초기설정', default = '')
            
            window_now = 'news_select'
            
        elif window_now == 'news_select':
            user_news = pg.confirm(text = '뉴스 사이트를 골라주세요', title = 'My Kiosk - 초기설정', buttons = ['네이버', '다음', 'Google', '뒤로가기'])
            if user_news == '네이버':
                user_news = 'naver'
                window_now = 'name_select' 
                
            elif user_news == '다음':
                user_news = 'daum'
                window_now = 'name_select' 
                
            elif user_news == 'Google':
                user_news = 'google'
                window_now = 'name_select'
                
            elif user_news == '뒤로가기':
                window_now = 'browser_select'
               
        elif window_now == 'name_select':
            user_name = pg.prompt(text = '이름을 입력해주세요', title = 'My Kiosk - 초기설정', default = '')
            window_now = 'ask_fin'
                
        elif window_now == 'ask_fin':
            is_finish = pg.confirm(text = '이대로 설정하시겠습니까?', title = 'My Kiosk - 초기설정', buttons = ['예', '아니오'])
            if is_finish == '예':
                window_now = 'setting_finish'
                pg.alert(text = '설정이 완료되었습니다.', title = 'My Kiosk - 초기설정', button = '확인')
                
                setting_value = user_browser + '/' + user_news + '/' + user_name
                initial.file_reWrite(setting_value)
            
            
            elif is_finish == '아니오':
                window_now = 'browser_select'

user_setting = initial.file_read().split('/') 
print(user_setting)
user_browser = user_setting[0]
user_name = user_setting[2]

window_now = 'main'
while window_now != 'all_clear':
    if window_now =='main':
        window_now = pg.confirm(text='원하는 항목을 선택해주세요.',title=user_name+'의 Kiosk - 메인화면',buttons=['실행', '설정'])
    if window_now == '실행':
        todo = pg.confirm(text='원하는 항목을 선택해주세요.',title=user_name+'의 Kiosk - 실행',buttons=['뉴스 랭킹','날씨','유튜브','구글 검색', '메일'])     
        if todo == '뉴스 랭킹': #사용자가 뉴스 랭킹 클릭
            os_start(user_browser, 'https://news.naver.com/main/ranking/popularDay.naver')
            pg.sleep(3) #뉴스 랭킹 페이지 이동 후 로딩
        
            news_1st_img = r'imgs\1.png'#숫자 1 이미지
            news_1st_button = pg.locateCenterOnScreen(news_1st_img, grayscale=True, confidence = 0.9)
            pg.moveTo(news_1st_button)#숫자 1 이미지로 마우스 이동
            pg.move(40, 0)#x좌표를 40만큼 이동하기
            pg.click()#기사 클릭하기
            window_now = 'all_clear'
            

        elif todo == '날씨':#사용자가 날씨 선택
            os_start(user_browser, 'https://www.google.com/search?q=날씨&sourceid=chrome&ie=UTF-8')
            #날씨 정보 사이트로 이동
            window_now = 'all_clear'
            
        elif todo == '유튜브':#사용자가 유튜브 선택
            os_start(user_browser, 'https://www.youtube.com/feed/subscriptions')#함수 실행
            pg.sleep(3) #유튜브 구독 페이지로 이동
        
            first_img = r'imgs\first.png'#'최신순'이미지 탐색
            first_button = pg.locateCenterOnScreen(first_img, grayscale=True, confidence= 0.9)
            pg.moveTo(first_button)#탐색한 이미지로 마우스 이동
            pg.move(0, 50)#y좌표로 50만큼 이동
            pg.click()#가장 최근 영상을 클릭하여 재생
            window_now = 'all_clear'

        elif todo == '구글 검색': #사용자가 구글 검색 선택
            #prompt창을 이용하여 검색하고자 하는 내용 입력받기
            keyword = pg.prompt(text = '검색어를 입력하세요', title = '구글 검색', default = '')
        
            #검색하고자 하는 키워드를 조합하여 주소 완성
            search = 'https://www.google.com/search?q='+ keyword+'&sourceid=chrome&ie=UTF-8'
        
            os_start(user_browser, search)#함수 실행하여 검색 완료
            window_now = 'all_clear'
            
    elif window_now == '설정':
        window_now = pg.confirm(text='원하는 항목을 선택해주세요.',title=user_name+'의 Kiosk - 설정',buttons=['초기화', '사용자 설정', '돌아가기'])
        if window_now == '초기화':
            all_clear = pg.prompt(text = "초기화하시려면 '초기화'를 입력해 주세요.", title = user_name+'의 Kiosk - 초기화', default = '')
            if all_clear == '초기화':
                #initial.file_reWrite('0')
                pg.alert(text = '초기화가 완료되었습니다. \n프로그램을 다시 실행시켜주세요', title = user_name+'의 Kiosk - 초기화 완료', button = '확인')
                window_now == 'all_clear'
        elif window_now =='사용자 설정':
            pass
        elif window_now =='돌아가기':
            window_now = 'main'
print()
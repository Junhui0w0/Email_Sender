import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import shutil
import tkinter
import tkinter.font
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import time
from tkinter import messagebox  # 들어가야함

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# GUI생성
root = Tk()
root.title("Email Sender Project")
root.geometry("900x600")

root.option_add("*Font", "맑은고딕 17") #전체 폰트 설정.
font = tkinter.font.Font(family="맑은고딕", size=30)
email_font = tkinter.font.Font(family="맑은고딕", size=15)

# 이메일 텍스트 라벨
email_lbl = Label(root)
email_lbl.place(x=5,y=5)
email_lbl.config(text="이메일 내용 입력", font=font)


# 이메일 텍스트 입력
email_txt = Text(root)
email_txt.place(x=5,y=50)
email_txt.config(width="45", height="12", font=email_font)

# # 공백1
# cleanlab1 = Label(root)
# cleanlab1.config(text="")
# cleanlab1.pack()


# 첨부파일 라벨
FileLabel = Label(root)
FileLabel.place(x=500, y= 5)
FileLabel.config(text="첨부 파일 선택", font=font)


#첨부파일 선택
FileEntry = Button(root)
FileEntry.place(x=600,y=50)
FileEntry.config(text="클릭",font=font, background='yellow')


# 이메일 등록 라벨
email_register_lbl = Label(root)
email_register_lbl.place(x=5, y= 300)
email_register_lbl.config(text="이메일 등록", font=font)


#이메일 등록 txt
email_register_txt = Text(root)
email_register_txt.place(x=5,y=345)
email_register_txt.config(width="45", height="3", font=email_font)

#이메일 등록 btn
email_register_btn = Button(root)
email_register_btn.place(x=420, y=300)
email_register_btn.config(text="등록",background='yellow')


# 이름/이메일 검색 라벨
search_lbl = Label(root)
search_lbl.place(x=5, y= 430)
search_lbl.config(text="이메일, 이름 검색")

#이름/이메일 수정 btn
email_edit_btn = Button(root)
email_edit_btn.place(x=350, y=430)
email_edit_btn.config(text="수정",background='yellow')

#이름/이메일 삭제 btn
email_del_btn = Button(root)
email_del_btn.place(x=420, y=430)
email_del_btn.config(text="삭제",background='yellow')

#이름/이메일 검색 txt
search_txt = Entry(root)
search_txt.place(x=5,y=475)
search_txt.config(width="45",font=email_font)

#이름/이메일 검색 lbl
result_lbl = Label(root)
result_lbl.place(x=5, y=500)
result_lbl.config(text="검색 결과:", foreground="blue")

#네이버/다음/지메일 선택 RadioBtn
var = IntVar()
naver_rb = Radiobutton(root, text="네이버", variable=var, value=1, foreground='green')
naver_rb.place(x= 660, y=450)

# daum_rb = Radiobutton(root, text="다음", variable=var, value=2, foreground='blue')
# daum_rb.place(x= 660, y=480)

# gmail_rb = Radiobutton(root, text="지메일", variable=var, value=3, foreground='black')
# gmail_rb.place(x= 660, y=510)

def url_select():
    #만약 배포할 생각이라면, 아래 chromdrvier.exe 경로를 직접 선택하게 해야할 듯 ?
    s= Service("C:\\Users\\wydyx\\OneDrive\\바탕 화면\\준희\\프로그래밍\\Python\\!기타활동\\Project\\Email-Sender\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=s, options=options)

    if(var.get() == 1): 
        login_url = 'https://mail.naver.com/v2/new'
        xpath_email_receiver = "//input[@class='user_input']" #O
        xpath_email_title = "//input[@id='subject_title']" #X
        xpath_email_file = "//input[@id='ATTACH_LOCAL_FILE_ELEMENT_ID']"
        xpath_email_send = "//button[@class='button_write_task']"

    # elif(var.get() == 2):
    #     login_url = '다음'
    # elif(var.get() == 3):
    #     login_url = 'https://mail.google.com/mail/u/0/#inbox?compose=new'


    driver.get(url=login_url) #var에 따라 xpath 경로 달라짐
    driver.implicitly_wait(150)

    driver.find_element(By.XPATH,xpath_email_receiver).send_keys("wydyxh@gmail.com")  #이메일을 받는 사람
    driver.implicitly_wait(100)

    driver.find_element(By.XPATH,xpath_email_title).send_keys("TEST1") #이메일 제목
    driver.implicitly_wait(100)

    #driver.find_element(By.XPATH,xpath1).submit("") #첨부파일은 send_keys ? submit ?
        #정 안되면 첨부파일을 메일창에서 직접 클릭하는 방법으로 진행

    driver.find_element(By.XPATH, xpath_email_file).send_keys("C:\\Users\\wydyx\\OneDrive\\바탕 화면\\준희\\test.pdf")
    driver.implicitly_wait(10)
    
    driver.find_element(By.XPATH,xpath_email_send).click() #이메일 전송
    driver.implicitly_wait(10)

#이메일 전송 btn
email_send = Button(root)
email_send.place(x=800, y=530)
email_send.config(text="이메일 \n전송",background="yellow", command=url_select)

#이메일 전송 웹사이트 선택 Label
send_lbl = Label(root)
send_lbl.config(text="로그인 웹사이트 선택",foreground='red')
send_lbl.place(x=660,y=420)


root.mainloop()
#login.py 필요없이 , '이메일 전송' 버튼 누르면 바로 이메일 보내는 site 염
#   -> 자동으로 로그인 페이지 뜸 (수동으로 해야 함 (매크로방지))
#   -> 제목, 내용, 첨부파일 전부 실행
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

import tkinter
import tkinter.font
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


# GUI생성
root = Tk()
root.title("Email Sender Project")
root.geometry("1500x900")

root.option_add("*Font", "맑은고딕 17") #전체 폰트 설정.
font = tkinter.font.Font(family="맑은고딕", size=30)
email_font = tkinter.font.Font(family="맑은고딕", size=25)


#[Title] 이메일 제목 Position
email_title_x = 5
email_title_y = 100

#[Title] 이메일 제목 Label
email_title_lbl = Label(root)
email_title_lbl.place(x=email_title_x, y=email_title_y)
email_title_lbl.config(text="이메일 제목", font=font, foreground="green")

#[Title] 이메일 제목 Entry
email_title_entry = Entry(root)
email_title_entry.place(x=email_title_x, y=email_title_y + 50)
email_title_entry.config(width="45", font=email_font)



#[Registering] 이메일 등록 Position
email_register_x = email_title_x
email_register_y = email_title_y + 150

#[Registering] 이메일 등록 Label
email_register_lbl = Label(root)
email_register_lbl.place(x=email_register_x, y=email_register_y)
email_register_lbl.config(text="이메일 등록 ex)이름 이메일", font=font, foreground="green")

#[Registering] 이메일 등록 Entry
email_register_txt = Entry(root)
email_register_txt.place(x=email_register_x, y=email_register_y + 50)
email_register_txt.config(width="45", font=email_font)

#[Registering] 이메일 등록버튼 Function
def func_email_add():
    lst = email_register_txt.get().split(' ')
    with open(email_path, "a", encoding="utf-8") as file:
        file.write(f"{lst[0]} {lst[1]}\n")

    with open(email_path, "r", encoding="utf-8") as file:
        name_email = file.read()
    
    show_registered_email_lbl.config(background="purple", font=font2, foreground="white",
                                 text=name_email)

    email_register_txt.delete(0, END)

#[Registering] 이메일 등록 Button
email_register_btn = Button(root)
email_register_btn.place(x=email_register_x + 800, y=email_register_y)
email_register_btn.config(text="등록",background='yellow', command=func_email_add)



#[Search] 이름/이메일 검색 Position
email_search_x = email_title_x
email_search_y = email_title_y + 270

#[Search] 이름/이메일 검색 Label
search_lbl = Label(root)
search_lbl.place(x=email_search_x, y= email_search_y)
search_lbl.config(text="이메일 혹은 이름 검색", foreground="green", font=email_font)

#[Search] 이름/이메일 검색 Entry
search_txt = Entry(root)
search_txt.place(x=email_search_x, y=email_search_y + 50)
search_txt.config(width="45",font=email_font)

#[Search] 이름/이메일 검색 Label
result_lbl = Label(root)
result_lbl.place(x=email_search_x, y=email_search_y + 100)
result_lbl.config(text="[검색 결과]", foreground="blue")

#[Search-Edit] 이름/이메일 수정 Button
email_edit_btn = Button(root)
email_edit_btn.place(x=email_search_x+730, y=email_search_y)
email_edit_btn.config(text="수정",background='yellow')

#[Search-Delete] 이름/이메일 삭제 Function
def delete_email_func():
    input_data = search_txt.get()
    
    name_lst = []
    email_lst = []

    with open("email_receiver.txt", "r", encoding="utf-8") as file:
        name_and_email = file.read()

    lst = name_and_email.split('\n')
    #print(lst) #디버깅
    lst.pop(-1)

    for data in lst:
        name = data.split(' ')[0]
        email = data.split(' ')[1]

        name_lst.append(name)
        email_lst.append(email)

    idx = 'INDEX'
    if '@' in input_data: #입력한 데이터가 이메일 일 때
        try:
            idx = email_lst.index(input_data)
        except ValueError:
            messagebox.showinfo("Error", "해당 이메일이 존재하지 않습니다.")
            return 0
    else:
        try:
            idx = name_lst.index(input_data)
        except ValueError:
            messagebox.showinfo("Error", "해당 이름이 존재하지 않습니다.")
            return 0

    if idx == 'INDEX':
        return 0
    else:
        #1. email_receiver.txt 내용 불러오기
        with open("email_receiver.txt", "r", encoding="utf-8") as file:
            data = file.read()

        data_lst = data.split('\n')

        #2. index가 idx번째인 내용을 lst에서 삭제
        data_lst.pop(idx)

        #3.email_receiver.txt에 다시 저장
        string_data = '\n'.join(data_lst)
        with open("email_receiver.txt", "w", encoding="utf-8") as file:
            file.write(string_data)

        #4. show_registered_email_lbl에 email_receiver.txt 내용 입력
        with open("email_receiver.txt", "r", encoding="utf-8") as file:
            name_email = file.read()
    
        show_registered_email_lbl.config(background="purple", font=font2, foreground="white",
                                    text=name_email)

        search_txt.delete(0, END)


#[Search-Delete] 이름/이메일 삭제 Button
email_del_btn = Button(root)
email_del_btn.place(x=email_search_x + 800, y=email_search_y)
email_del_btn.config(text="삭제",background='yellow', command=delete_email_func)


#[File] 이메일 첨부파일 Position
file_attatch_x = email_title_x
file_attatch_y = email_title_y + 500

#[File] 이메일 첨부파일 Label
FileLabel = Label(root)
FileLabel.place(x=file_attatch_x, y=file_attatch_y)
FileLabel.config(text="첨부 파일 선택", font=font, foreground="green")

#[File] 이메일 첨부파일 버튼 Function
file_attach_path=""
def func_file_attach():
    global file_attach_path
    file_attach_path = filedialog.askopenfile()
    file_attatch_path_lbl.config(text=file_attach_path.name)

#[File] 첨부파일 Button
FileEntry = Button(root)
FileEntry.place(x=file_attatch_x,y=file_attatch_y + 45)
FileEntry.config(text="클릭",font=font, background='yellow', command=func_file_attach)

#[File] 첨부파일 경로 Label
file_attatch_path_lbl = Label(root)
file_attatch_path_lbl.place(x=file_attatch_x, y=file_attatch_y + 120)
file_attatch_path_lbl.config(text=file_attach_path, foreground="red")



#[Select] 이메일 전송 사이트 Position
email_select_x = email_title_x + 400
email_select_y = email_title_y + 500

#[Select] 이메일 전송 웹사이트 선택 Label
send_lbl = Label(root)
send_lbl.config(text="로그인 웹사이트 선택",foreground='red')
send_lbl.place(x=email_select_x,y=email_select_y)

#[Select] 네이버/다음/지메일 선택 RadioBtn
var = IntVar()
naver_rb = Radiobutton(root, text="네이버", variable=var, value=1, foreground='green')
naver_rb.place(x= email_select_x, y=email_select_y + 30)

# daum_rb = Radiobutton(root, text="다음", variable=var, value=2, foreground='blue')
# daum_rb.place(x= 660, y=480)

# gmail_rb = Radiobutton(root, text="지메일", variable=var, value=3, foreground='black')
# gmail_rb.place(x= 660, y=510)

name_lst = []
def url_select():
    global name_lst
    #만약 배포할 생각이라면, 아래 chromdrvier.exe 경로를 직접 선택하게 해야할 듯 ?
    s= Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=s, options=options)

    if(var.get() == 1): 
        login_url = 'https://mail.naver.com/v2/new'
        xpath_email_receiver = "//input[@class='user_input']" #이메일 수신자
        xpath_email_title = "//input[@id='subject_title']" #이메일 제목
        xpath_email_file = "//input[@id='ATTACH_LOCAL_FILE_ELEMENT_ID']" #이메일 첨부파일
        xpath_email_send = "//button[@class='button_write_task']" #이메일 전송 버튼

    # elif(var.get() == 2):
    #     login_url = '다음'
    # elif(var.get() == 3):
    #     login_url = 'https://mail.google.com/mail/u/0/#inbox?compose=new'


    driver.get(url=login_url) #var에 따라 xpath 경로 달 라짐
    driver.implicitly_wait(150)

    name_lst = []
    email_lst = []

    with open("email_receiver.txt", "r", encoding="utf-8") as file:
        name_and_email = file.read()

    lst = name_and_email.split('\n')
    #print(lst) #디버깅
    lst.pop(-1)

    for data in lst:
        name = data.split(' ')[0]
        email = data.split(' ')[1]

        name_lst.append(name)
        email_lst.append(email)

    for email in email_lst:
        driver.find_element(By.XPATH,xpath_email_receiver).send_keys(email+' ')  #이메일을 받는 사람
        driver.implicitly_wait(100)

    driver.find_element(By.XPATH,xpath_email_title).send_keys(email_title_entry.get()) #이메일 제목
    driver.implicitly_wait(100)

    driver.find_element(By.XPATH, xpath_email_file).send_keys(file_attach_path.name) #이메일 첨부 파일
    driver.implicitly_wait(100)


#[Select] 이메일 전송 btn
email_send = Button(root)
email_send.place(x=email_select_x - 10, y=email_select_y + 100)
email_send.config(text="이메일 \n전송",background="yellow", command=url_select)



#[Checking-Registered] 등록된 이메일 Postion
registerd_email_x = email_title_x + 920
registerd_email_y = 5

#[Checking-Registered] 등록된 이메일 확인 Label
registerd_email_lbl = Label(root)
registerd_email_lbl.place(x=registerd_email_x, y=registerd_email_y)
registerd_email_lbl.config(text="등록된 이메일", foreground="purple", font=font)

#[Checking-Registered] 등록된 이메일 출력 Label
font2 = tkinter.font.Font(family="맑은고딕", size=15)
#print(os.getcwd())

email_path = "email_receiver.txt"
with open(email_path, "r", encoding="utf-8") as file:
    name_email = file.read()

    # print(name_lst)
    # print(email_lst) #디버깅

show_registered_email_lbl = Label(root)
show_registered_email_lbl.place(x=registerd_email_x, y=registerd_email_y+50)
show_registered_email_lbl.config(background="purple", font=font2, foreground="white",
                                 text=name_email)



root.mainloop()
#login.py 필요없이 , '이메일 전송' 버튼 누르면 바로 이메일 보내는 site 염
#   -> 자동으로 로그인 페이지 뜸 (수동으로 해야 함 (매크로방지))
#   -> 제목, 내용, 첨부파일 전부 실행

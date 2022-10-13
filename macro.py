#-*- coding: utf-8 -*-

import os
import time
import sys

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
#from tkinter import * # __all__
from tkinter import filedialog
from configparser import ConfigParser, ExtendedInterpolation

import pyautogui as agi
import pyperclip as pclip

from subprocess import Popen

def degis(value):
    global buton
    #buton["label"] = '%s'%({True: 'Thrust', False: 'Top'}[value])
    if(value == "1"):
        buton["label"] = "Thrust"
    else:
        buton["label"] = "Top"

#파일열기 실행

def fileOpen(path):
    workingDir=os.path.abspath(path)
    pclip.copy(workingDir)
    agi.press('enter')
    time.sleep(1)
    agi.hotkey('ctrl', 'o')
    time.sleep(1)   
    agi.hotkey('ctrl','v')
    agi.press('enter',interval=0.1)
    agi.press('n',interval=0.1)
    agi.hotkey('alt','v')
    agi.press('a')
    
# 파일 추가
def add_file():
    global files
    global workingFldr
    
    files = filedialog.askopenfilenames(title="데이터 파일을 선택하세요", \
        filetypes=(("Formpak Document(*.FPK)", "*.fpk"), ("모든 파일", "*.*")), \
        initialdir=workingFldr)
        # 최초에 사용자가 지정한 경로를 보여줌
        #         
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(tk.END, file)
    saveIni('GENERAL','working_dir',os.path.dirname(files[0]))    
    
# 선택 삭제
def del_file():
    
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

#리스트속 이미지 열기
def imgLoad(x):
    fileName='./image/%s.png'%dic[x]
    api=agi.locateCenterOnScreen(fileName,grayscale=True,confidence = 0.9)
    if not api:
        msgbox.showwarning('경고:%s 이미지를 찾을수 없습니다.'%x)
        sys.exit()
    return api

#상대포지션 클릭하기2
def clicker2(a,x,y):
    i,j=imagePosition[a]
    agi.click(i+x,j+y)

#상대포지션 클릭하기
def clicker(a,x,y):
    i,j=imagePosition[parTs[a]]
    #i,j=position[a]
    agi.click(i+x,j+y)

#x,y 값 키보드로 입력하기
def bottoms(x,y):
    clicker(1,32,5)#키입력
    agi.typewrite(x)
    agi.press('enter')
    clicker(1,32,5)#키입력
    agi.typewrite(y)
    agi.press('enter')

#축 회전후 피크점 잡기
def rotpeak(a,x,y):

    #회전
    clicker(0,30,63)#회전
    clicker(5,-29,37)#X축
    clicker(4,58,a)#선
    
    #피크점
    clicker(0,-28,-78)#피크점
    clicker(5,-90,-10)#X범위
    bottoms(x,y)

#메인
def thrust():
    
    #원점 설정하기
    clicker(0,-28,59)#원점설정
    clicker(5,-90,40)#결과선택
    clicker(4,58,58)#포인트1

    #버텀점
    clicker(0,30,-78)#버텀점
    clicker(5,-90,-10)#X범위
    
    #간격 입력
    bottoms('2','6')
    bottoms('6','10')
    bottoms('10','14')
    bottoms('14','17')

    #라인

    clicker(0,-88,-30)#선
    clicker(5,-90,40)#결과선택

    clicker(4,58,58)#포인트1
    clicker(4,58,95)#포인트2
    
    clicker(4,58,110)#포인트3
    clicker(4,58,95)#포인트2
    
    clicker(4,58,130)#포인트4
    clicker(4,58,110)#포인트3
    
    clicker(4,58,150)#포인트5
    clicker(4,58,130)#포인트4
    
    rotpeak(170,'0','4')

    #회전

    clicker(0,30,63)#회전
    clicker(5,-29,37)#X축
    clicker(4,58,185)#선2

    #피크점
    clicker(0,-28,-78)#피크점
    clicker(5,-90,-10)#X범위
    bottoms('4','8')

    #회전

    clicker(0,30,63)#회전
    clicker(5,-29,37)#X축
    clicker(4,58,200)#선3

    #피크점
    clicker(0,-28,-78)#피크점
    clicker(5,-90,-10)#X범위
    bottoms('8','12')


    clicker(0,30,63)#회전
    clicker(5,-29,37)#X축
    clicker(4,58,220)#선4

    #피크점
    clicker(0,-28,-78)#피크점
    clicker(5,-90,-10)#X범위
    bottoms('12','15')

    #거리
    clicker(0,-35,12)#거리
    clicker(5,-90,40)#결과선택
    clicker(4,58,260)#점6
    clicker(4,58,170)#선1
    clicker(4,58,290)#점7
    clicker(4,58,185)#선2
    clicker(4,58,330)#점8
    clicker(4,58,200)#선3
    clicker(4,58,365)#점9
    clicker(4,58,220)#선4

    clicker(4,58,110)#점3
    clicker(4,58,95)#점2

    clicker(4,58,130)#점4
    clicker(4,58,110)#점3

    clicker(4,58,150)#점5
    clicker(4,58,130)#점4

    #저장
    agi.hotkey('alt', 't')
    agi.press('r')
    time.sleep(1)   
    agi.hotkey('enter')
    agi.press('y',interval=0.1)

def top():
    #원점 설정하기
    clicker(0,-28,59)#원점설정
    clicker(5,-90,40)#결과선택
    clicker(4,58,75)#포인트2

    clicker(0,-88,-78)#점
    clicker(5,-25,-52)#측정점
    clicker(1,32,5)#키입력
    agi.typewrite('0.2')
    agi.press('enter')   

    

    #1.8mm 점 측정
    clicker(0,-88,-78)#점
    clicker(5,-25,-52)#측정점
    clicker(1,32,5)#키입력
    agi.typewrite('1.7')
    agi.press('enter')    

    clicker(0,-88,-30)#선
    clicker(5,-90,40)#결과선택
    clicker(4,58,105)#0.2점
    clicker(4,55,130)#1.8점

    #축회전
    clicker(0,30,63)#회전
    clicker(5,-29,37)#X축
    clicker(4,58,150)#1.8선

    
    clicker(0,-88,-78)#점
    clicker(5,32,-56)#X값
    clicker(1,32,5)#키입력
    agi.typewrite('2')
    agi.press('enter')    

    clicker(3,-88,19)#반복실행
    agi.hotkey('tab')
    agi.hotkey('tab')
    agi.typewrite('2')
    agi.press('enter')
    agi.hotkey('shift','tab')  
    agi.typewrite('12')
    agi.press('enter')    
    agi.press('enter')
    agi.press('enter')
    agi.press('esc')

    clicker(0,-92,11)#좌표차
    
    clicker(4,55,75)#원점
    clicker(4,55,185)#점2
    clicker(4,55,75)#원점
    clicker(4,55,200)#점2
    clicker(4,55,75)#원점
    clicker(4,55,220)#점2
    clicker(4,55,75)#원점
    clicker(4,55,235)#점2
    clicker(4,55,75)#원점
    clicker(4,55,255)#점2
    clicker(4,55,75)#원점
    clicker(4,55,270)#점2
    clicker(4,55,75)#원점
    clicker(4,55,290)#점2
    clicker(4,55,75)#원점
    clicker(4,55,310)#점2
    clicker(4,55,75)#원점
    clicker(4,55,330)#점2
    clicker(4,55,75)#원점
    clicker(4,55,345)#점2
    clicker(4,55,75)#원점
    clicker(4,55,360)#점2
    clicker(4,55,75)#원점
    clicker(4,55,385)#점2
    clicker(4,55,75)#원점
    clicker(4,55,400)#점2
    clicker(4,55,75)#원점
    clicker(4,55,60)#점1

    #저장
    agi.hotkey('alt', 't')
    agi.press('r')
    time.sleep(1)   
    agi.hotkey('enter')
    agi.press('y',interval=0.1)

def runprg(): 
    global executeFile   
    if not executeFile:
        executeFile=getProgramFile()
    try: 
        Popen(executeFile)
    except FileNotFoundError:
        executeFile=getProgramFile(executeFile)
    time.sleep(2)
    agi.press('enter',interval=0.1)
    time.sleep(2)

def getProgramFile (a):
        
    file = filedialog.askopenfilenames(title="Formtracer 프로그램 파일 위치를 지정하세요", \
        filetypes=(("Formtrack EXE(*.EXE)", "*.exe"), ("모든 파일", "*.*")), \
        initialdir=os.path.dirname(a))
    
    saveIni('EXTERNAL','formtrack',file[0])

    return file[0]

def ask_file():
    pass

def start():
    global files
    global buton
    if not files:
        msgbox.showwarning("경고", "데이터 파일을 추가하세요")
        return
    
    if not agi.getWindowsWithTitle("FORMTRACE"):
        runprg()
        time.sleep(10)

    w=agi.getWindowsWithTitle("FORMTRACE")[0]
    w.activate()

    #agi.PAUSE(1)
        
    #타이틀바 클릭하기
    tiTle=imgLoad('title')
    agi.click(tiTle)
    agi.hotkey('ctrl','n')
    agi.press('enter',interval=0.1)
    
    for fName in files:
        fileOpen(fName)
        time.sleep(1)
        
        if not imagePosition:
            #화면 읽기
            for partName in parTs:
                imagePosition[partName]=imgLoad(partName)
                    
        if buton['label']=='Thrust':thrust()
        else:top()
    
    
def configure(a,b,c):
    try : return config.get(a,b)
    except :
        if not config.has_section(a):
            config.add_section(a)
        saveIni(a,b,c)
        return c

def saveIni(a,b,c):
    config.set(a,b,c)
    configFile = open("config.ini", "w",encoding='cp949')
    config.write(configFile)
    configFile.close()

config = ConfigParser(interpolation=ExtendedInterpolation())
config_file_path = 'config.ini'
config.read(config_file_path,encoding='cp949')
aexecute=r"C:\Program Files (x86)\MitutoyoApp\Formtracepak\Formtracepak.exe"
adic=dict(customize='custom',input='input',title='titlebar',user_mark='result2',part='parts',result='result')
#position=list()
agi.FAILSAFE = True
agi.PAUSE=0.1
dic=dict()
imagePosition=dict()

if config.has_section('IMAGE'):
    for item in config.options('IMAGE'):
        dic[item]=configure ('IMAGE',item,adic[item])
else : 
    for item in adic.keys():
        dic[item]=configure ('IMAGE',item,adic[item])


workingFldr=configure ('GENERAL','working_dir',os.path.abspath('.'))
executeFile=configure ('EXTERNAL','formtrack',aexecute)

parTs=list(dic.keys())

root = tk.Tk()
root.iconbitmap("top.ico")
root.title("Top File Macro")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = tk.Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # 간격 띄우기

btn_add_file = tk.Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = tk.Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

buton = tk.Scale(file_frame, orient = tk.HORIZONTAL,length = 50,to = 1,showvalue = False,sliderlength = 25,label = "Top",command = degis)
buton.pack(side='top')

# 리스트 프레임
list_frame = tk.Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = tk.Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 실행 프레임
frame_run = tk.Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = tk.Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = tk.Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

btn_run = tk.Button(frame_run, padx=5, pady=5, text="측정기 실행", width=12, command=runprg)
btn_run.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()



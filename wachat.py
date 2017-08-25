import subprocess
from tkinter import *
root = Tk()

def wachat():
    n = 0
    while(n!=int(wachatLNum.get())):
        subprocess.Popen(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe",shell=True)
        n +=1
wachatLF = LabelFrame(root,text="微信",font = ("黑体","20"),padx=1,pady=1)
wachatLF.pack()
wachatLNum =Spinbox(wachatLF,width = 10,font= ("雅黑","25"),\
                     justify = CENTER,from_ = 2,to = 99)
wachatLNum.pack()

BackBtn = Button(root,text = "启动",font= ("雅黑","25"),command = wachat)
BackBtn.pack()
mainloop()



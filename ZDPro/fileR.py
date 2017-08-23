import os
import os.path
import time
import datetime
import pickle
import send

nowpath = os.getcwd()
os.chdir(os.pardir)
prepath = os.getcwd()
os.chdir(nowpath)
text = ["","",""]
def FileR(datime):
    DateT = datime.strftime("%Y%m%d")
    Datey = datime.strftime("%Y")
    Datem = datime.strftime("%m")
    Filepath = os.path.join(prepath ,Datey , Datem)
    Filetxt = os.path.join(Filepath , DateT)
    if not(os.path.exists(Filepath)):
        os.makedirs(Filepath)
    try:
        f= open(Filetxt ,'rb')
        return pickle.load(f)
    except FileNotFoundError:
        f = open(Filetxt ,"ab")
        pickle.dump('',f)
        f.close()
        f= open(Filetxt ,'rb')
        return pickle.load(f)
    finally:
        f.close()
def FileW(text,datime):
    DateT = datime.strftime("%Y%m%d")
    Datey = datime.strftime("%Y")
    Datem = datime.strftime("%m")
    Filepath = os.path.join(prepath ,Datey , Datem)
    Filetxt = os.path.join(Filepath , DateT)
    try:
        f= open(Filetxt,'wb')
        pickle.dump(text,f)
        f.close()
    finally:
        f.close()
        messDT = datetime.datetime.today()
        mess = messDT.strftime("%Y%m%d%H%M%S")
        send.pushfile(Filepath,prepath + "\\sign" ,mess)#函数
        
def Redata(datime,Sdata,Edata,filename):
    DateT = datime.strftime("%Y%m%d")
    Filetxt = prepath + "\\sign\\" + filename
    try:
        f= open(Filetxt ,'rb')
        DanF = pickle.load(f)
        if DanF[0] == DateT and int(DanF[1]) > Sdata:
            return DanF
            f.close()        
    except FileNotFoundError:
        f= open(Filetxt,'ab')
        f.close()
        f = open(Filetxt,'wb')
        text[0] = DateT
        text[1] = str(Sdata)
        text[2] = str(Edata)
        pickle.dump(text,f)
    finally:
        f.close()
def Wrdata(datime,Sdata,Edata,filename):
    DateT = datime.strftime("%Y%m%d")
    Filetxt = prepath + "\\sign\\" + filename
    try:
        f = open(Filetxt,'wb')
        text[0] = DateT
        text[1] = str(Sdata)
        text[2] = str(Edata)
        pickle.dump(text,f)
    finally:
        f.close()
    

if __name__ == '__main__':
    pass

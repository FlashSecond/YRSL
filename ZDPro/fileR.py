import os
import os.path
import time
import datetime
import pickle

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
        time.sleep(0.2)
        f.close()
        
    finally:
        f.close()
        
def Redata(datime,Sdata,Edata,filename):
    DateT = datime.strftime("%Y%m%d")
    Filetxt = "sign\\" + filename
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
    Filetxt = "sign\\" + filename
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

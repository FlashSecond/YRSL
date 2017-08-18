import os
import os.path
import time
import datetime
import pickle
nowpath = os.getcwd()
os.chdir(os.pardir)
prepath = os.getcwd()
os.chdir(nowpath)
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
    finally:
        f.close()
def Redata(datime,Sdata,Edata,filename):
    DateT = datime.strftime("%Y%m%d")
    Filetxt = "sign\\" + filename + ".txt"
    try:
        f= open(Filetxt ,'r')
        DanF = f.readlines()
        if DanF[0][:-1] == DateT and int(DanF[1][:-1]) > Sdata:
            return DanF
            f.close()        
    except FileNotFoundError:
        f= open(Filetxt,'a')
        f.close()
        f = open(Filetxt,'w')
        f.writelines(DateT + '\n' + str(Sdata) + '\n' + str(Edata) + '\n')
        f.flush()
        f.close()
    finally:
        f.close()
def Wrdata(datime,Sdata,Edata,filename):
    DateT = datime.strftime("%Y%m%d")
    Filetxt = "sign\\" + filename + ".txt"
    try:
        f = open(Filetxt,'w')
        f.writelines(DateT + '\n' + str(Sdata) + '\n' + str(Edata) + '\n')
        f.flush()
    finally:
        f.close()
    

if __name__ == '__main__':
    pass

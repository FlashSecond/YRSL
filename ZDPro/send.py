import os
import os.path
prepath = os.getcwd()

def sendinfo():
    nowpath ='\"' + prepath + '\\' + "send.exe\""
    os.system(nowpath)

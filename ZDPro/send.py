import os
import os.path
prepath = os.getcwd()

def sendinfo():
    nowpath ='\"' + prepath + '\\' + "send.exe\""
    os.system(nowpath)

def pullfile():
    pull = "cd /d %s &\
git pull https://github.com/FlashSecond/YRSL.git &" % (prepath)
    os.system(pull)
def pushfile(mess):
    push = "cd /d %s &\
git add . &\
git commit -m %s &\
git push origin master &" % (prepath,mess)
    os.system(push)

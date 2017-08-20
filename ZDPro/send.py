import os
import os.path
bepath = os.getcwd()
os.chdir(os.pardir)
prepath = os.getcwd()
os.chdir(bepath)
def sendinfo():
    nowpath ='\"' + bepath + '\\' + "send.exe\""
    os.system(nowpath)

def pullfile():
    pull = "cd /d %s &\
git pull origin master &" % (prepath)
    os.system(pull)
def pushfile(NOF,NOS,mess):
    push = "cd /d %s &\
git add %s %s &\
git commit -m %s &\
git push origin master &" % (prepath,NOF,NOS,mess)
    os.system(push)

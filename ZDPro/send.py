import os
import subprocess
bepath = os.getcwd()
os.chdir(os.pardir)
prepath = os.getcwd()
os.chdir(bepath)
def sendinfo():
    nowpath ='\"' + bepath + '\\' + "send.exe\""
    subprocess.Popen(nowpath,shell = True)

def pullfile():
    pull = "cd /d %s &\
git pull origin master &" % (prepath)
    subprocess.Popen(pull,shell = True)
def pushfile(NOF,NOS,mess):
    push = "cd /d %s &\
git add %s %s &\
git commit -m %s &\
git push origin master &" % (prepath,NOF,NOS,mess)
    subprocess.Popen(push,shell = True)

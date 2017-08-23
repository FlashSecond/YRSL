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
    a = subprocess.Popen(pull,shell = True)
    a.wait()
def pushfile(NOF,NOS,mess):
    push = "cd /d %s &\
git add %s %s &\
git commit -m %s &\
git push origin master &" % (prepath,NOF,NOS,mess)
    a = subprocess.Popen(push,shell = True)
if __name__ == '__main__':
    pass


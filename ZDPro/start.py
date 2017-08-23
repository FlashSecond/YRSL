import os
import time
import subprocess
bepath = os.getcwd()
os.chdir(os.pardir)
prepath = os.getcwd()
os.chdir(bepath)
def startload(mess):
   # firpath ="cd /d %s &\
#git pull origin master & exit" % (prepath)
    firpath = "git add -A &\
git commit -m %s &\
git push origin master & \
cd /d %s &\
git pull origin master &\
git add -A &\
git commit -m %s &\
git push origin master & " % (mess,prepath,mess)
    a=subprocess.Popen(firpath,shell = True)
    a.wait()

def startup():
    secpath ='\"' + bepath + '\\' + "jiemian.pyw\""
    subprocess.Popen(secpath,shell = True)
    
if __name__ == '__main__':
    startload("Upload")
    startup()


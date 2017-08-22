import os
import time
import subprocess
bepath = os.getcwd()
os.chdir(os.pardir)
prepath = os.getcwd()
os.chdir(bepath)
def startload():
#    firpath ="cd /d %s &\
#git pull origin master &" % (prepath)
    firpath = '\"' + prepath + '\\' + "upload.py\""
    a = subprocess.Popen(firpath,shell = True)
    a.wait()
    secpath ='\"' + bepath + '\\' + "jiemian.pyw\""
    subprocess.check_call(secpath,shell = True)

if __name__ == '__main__':
    startload()


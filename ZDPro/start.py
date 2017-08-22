import os
import time
import subprocess
bepath = os.getcwd()
os.chdir(os.pardir)
prepath = os.getcwd()
os.chdir(bepath)
def startload():
    #firpath ="cd /d %s &\
#git pull origin master & exit" % (prepath)
    firpath = '\"' + prepath + '\\' + "upload.py\""
    subprocess.check_call(firpath,shell = True)
    secpath ='\"' + bepath + '\\' + "jiemian.pyw\""
    os.system(secpath)
if __name__ == '__main__':
    startload()


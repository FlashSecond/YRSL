import os
import time
import subprocess
bepath = os.getcwd()
os.chdir(os.pardir)
prepath = os.getcwd()
os.chdir(bepath)
def startload():
    firpath ='\"' + prepath + '\\' + "upload.py\""
    secpath ='\"' + bepath + '\\' + "jiemian.pyw\""
    subprocess.Popen(firpath,shell = True)
    time.sleep(20)
    subprocess.Popen(secpath,shell = True)

if __name__ == '__main__':
    startload()

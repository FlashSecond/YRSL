import os
import time
import subprocess
bepath = os.getcwd()
os.chdir(os.pardir)
prepath = os.getcwd()
os.chdir(bepath)
def startload():
    firpath ='\"' + prepath + '\\' + "upload.py\""
    subprocess.call(firpath,shell = True)
    secpath ='\"' + bepath + '\\' + "jiemian.pyw\""
    subprocess.call(secpath,shell = True)

if __name__ == '__main__':
    startload()

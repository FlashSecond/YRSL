import os
import time
import subprocess
bepath = os.getcwd()
os.chdir(os.pardir)
prepath = os.getcwd()
os.chdir(bepath)
def startload():
    nowpath ='\"' + prepath + '\\' + "upload.py\""
    subprocess.call(nowpath,shell = True)

def startup():
    nowpath ='\"' + bepath + '\\' + "jiemian.pyw\""
    subprocess.Popen(nowpath,shell = True)

if __name__ == '__main__':
    startload()
    time.sleep(5)
    startup()


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
    fir = subprocess.call(firpath,shell = True)
    print(fir)
    if fir==0:
        print(fir)
        subprocess.Popen(secpath,shell = True)

if __name__ == '__main__':
    startload()

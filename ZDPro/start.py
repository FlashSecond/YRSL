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
    a=subprocess.Popen(firpath,shell = True)
    while(a.poll() == None):
        time.sleep(0.1)
        print(a.poll())
        pass
    else:
        print(a.poll())
        secpath ='\"' + bepath + '\\' + "jiemian.pyw\""
        subprocess.Popen(secpath,shell = True)
        
    
if __name__ == '__main__':
    startload()


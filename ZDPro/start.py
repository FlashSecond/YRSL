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
    os.system(firpath)
    secpath ='\"' + bepath + '\\' + "jiemian.pyw\""
    subprocess.Popen(secpath,shell = True)
        
    
if __name__ == '__main__':
    startload()


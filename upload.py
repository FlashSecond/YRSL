import os
import subprocess
bepath = os.getcwd()

def pushfile(mess):
    push = "cd /d %s &\
git pull origin master &\
git add -A &\
git commit -m %s &\
git push origin master &" % (bepath,mess)
    print("上传中")
    subprocess.Popen(push,shell = True)
if __name__== "__main__":
    pushfile("upload")

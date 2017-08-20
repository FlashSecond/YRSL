import os
import subprocess
bepath = os.getcwd()

def pushfile(mess):
    push = "cd /d %s &\
git pull origin master &\
git add -A &\
git commit -m %s &\
git push origin master &" % (bepath,mess)
    subprocess.Popen(push,shell = True)
    print("上传完成")
if __name__== "__main__":
    pushfile("upload")

import threading
import Fazzaco

def startCase(username,ps):
    Fazzaco.chatStart(username, ps)

class startThread(threading.Thread):
    def __init__(self,username,ps):
        threading.Thread.__init__(self)
        self.username=username
        self.ps = ps
    def run(self):
        startCase(self.username,self.ps)

with open('username.txt','r') as f:
    usernamelist=f.readlines()

with open('password.txt','r') as f:
    pslist=f.readlines()

proclist=[]
for i in range(len(usernamelist)):
    thread = startThread(usernamelist[i].replace(r'\n',''),pslist[i].replace(r'\n',''))
    proclist.append(thread)

for proc in proclist:
    proc.start()
for proc in proclist:
    proc.join()
import praw
import time
import tkinter
import random
from tkinter import *
import requests
import sys

def upvote():

    m = 0
    n = 0
    j= 0
    q=int(txtid.get())


    proxies ={
    'https': 'https://gb.proxiware.com:2001',
    }
     
    url = 'http://www.reddit.com'

    response = requests.post(url, proxies=proxies)

    f2 = open(txtn.get(),'r')
    content=f2.read()
    id_pwd=content.splitlines()
    f2.close()
    print(id_pwd)
    x=[]
    y=[]
    for i in id_pwd:
        x.append(i.split()[0])
        y.append(i.split()[1])
    print(x)
    print(y)

    while j<q:
            
        uname=x[m]
        upass=y[n]
        m=m+1
        n=n+1
        j=j+1

        reddit = praw.Reddit(
            client_id="enter client id",
            client_secret="enter the secret id",
            user_agent="enter a unique name for console",
            username=uname,
            password=upass)

        submission=reddit.submission(url= txtl.get())
        submission.upvote()
        time.sleep(180)
    
    
window=Tk()
window.geometry("720x480")
window.title("KAMIBOT")

l1=Label (window,text="UPVOTE BOT",font=("Arial bold",50))
l1.grid(sticky=E)

Label (window,text="FILENAME:",font="none 10 bold").grid(row=1,column=0,sticky=W)

txtn= Entry(window,width=15,bg="white")
txtn.grid(row=1,column=0)

Label (window,text="LINK:",font="none 10 bold").grid(row=2,column=0,sticky=W)

txtl= Entry(window,width=15,bg="white")
txtl.grid(row=2,column=0)

Label (window,text="UPVOTES",font="none 10 bold").grid(row=3,column=0,sticky=W)

txtid= Entry(window,width=15,bg="white")
txtid.grid(row=3,column=0)

bt= Button(window,text="UPVOTE",font="none 10 bold",width=13,command= upvote )
bt.grid(row=4,column=0,sticky=W)

window.mainloop()


###################################################KOKORO###################################################


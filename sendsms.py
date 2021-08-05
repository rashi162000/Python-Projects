import requests #create request to website
import json #sends data at very high speed
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def sendsms(number,message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params={
        "authorization":'DQHSYFPlEJRhxwk1tj2ybrB8G0nqNfL3gipu9MIUK6W4TvC7szX2CGTtKJFNayLlqIriZHsWEfSpzen5',
        "sender_id":'TXTIND',
        "message":message,
        "language":'english',
        "route":'v3',
        "numbers":number
    }
    response=requests.get(url,params=params)
    a=response.json()
    print(a)
    return a.get("return")



def btnclick():
    num = textNumber.get()
    msg = textMsg.get("1.0",END)
    r = sendsms(num,msg)
    if r:
        showinfo("Send Success","successfully sent")
    else:
        showerror("Error","Oops! Something went wrong!")

# creating GUI
root=Tk()
root.title("message sender")
root.geometry("400x550")
font = ("Helvetica",22,"bold")
textNumber=Entry(root,font=font)
textNumber.pack(fill=X,pady=20)
textMsg=Text(root)
textMsg=textMsg.pack(fill=X,pady=10)
sendBtn=Button(root,text="Send SMS",command=btnclick)
sendBtn.pack()





root.mainloop()


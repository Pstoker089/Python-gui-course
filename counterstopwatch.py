#imports
from tkinter import *
from tkinter import messagebox
import time

root=Tk()
root.geometry("300x250")
root.title("Time counter")

hour=StringVar()
minute=StringVar()
second=StringVar()
hour.set("00")
minute.set("00")
second.set("00")

#entries and placements
hourentry=Entry(root,width=3,font=("arial",18,""),textvariable=hour)
hourentry.place(x=80,y=20)
minentry=Entry(root,width=3,font=("arial",18,""),textvariable=minute)
minentry.place(x=130,y=20)
secentry=Entry(root,width=3,font=("arial",18,""),textvariable=second)
secentry.place(x=180,y=20)


#functions
def submit():
    global hour
    try:
        temp=int(hourentry.get())*3600+int(minentry.get())*60+int(secentry.get())
    except:
        print("Please insert a correct value")
    while temp>=-1:
        mins,secs=divmod(temp,60)
        hours=0
        if mins>=60:
            hour,mins=divmod(mins,60)
        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(0.1)
        if temp==0:
            messagebox.showinfo("Time countdown","times out")
        temp-=1

#buttons
btn=Button(root,text="set time countdown",bd="5",command=submit)
btn.place(x=70,y=120)


root.mainloop()
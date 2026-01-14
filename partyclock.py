#essentials
from tkinter import *
from time import strftime
import tkinter.font as font
import random

root=Tk()
root.geometry("300x59")

#variables
clist=["red","orange","pink","blue","purple","cyan"]

#widgets
clock=Label(root,font=font.Font(size=35),bg="orange")

#functions
def time():
    timer=strftime("%H: %M: %S  %p")
    cchoice=random.choice(clist)
    clock.config(text=str(timer),bg=cchoice)
    clock.after(1000,time)

time()

#placement
clock.pack()

root.mainloop()
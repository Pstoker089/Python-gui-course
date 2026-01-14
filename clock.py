#essentials
from tkinter import *
from time import strftime
import tkinter.font as font

root=Tk()
root.geometry("300x59")


#widgets
clock=Label(root,font=font.Font(size=35),bg="orange")

#functions
def time():
    timer=strftime("%H: %M: %S  %p")
    clock.config(text=str(timer))
    clock.after(1000,time)

time()

#placement
clock.pack()

root.mainloop()
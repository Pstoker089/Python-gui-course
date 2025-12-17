#basics
from tkinter import *
import tkinter.font as font
import random
root=Tk()
root.geometry("700x400")

#variables
whowon=""
option=""
cchoice=""
choicelist=["rock","paper","scissors"]

#functions
def choose(option):
    cchoice=random.choice(choicelist)
    if option=="rock":
        if cchoice=="paper":
            whowon="COMPUTER WINS"
        elif cchoice=="scissors":
            whowon="PLAYER WINS"
    if option=="paper":
        if cchoice=="scissors":
            whowon=="COMPUTER WINS"
        elif cchoice=="rock":
            whowon="PLAYER WINS"
    if option=="scissors":
        if cchoice=="paper":
            whowon="PLAYER WINS"
        elif cchoice=="rock":
            whowon="COMPUTER WINS"
    if cchoice==option:
        whowon="TIE"




    


#cosmetics
root.title("Rock papaer scissors")
title=Label(root,text="Rock Paper Scissors",font=font.Font(size=20),fg="grey")
winstatus=Label(root,text="",fg="green")
optionstxt=Label(root,text="Your options:",fg="grey")
scoretxt=Label(root,text="Scores:",fg="grey")
Pselect=Label(root,text="")
Cselect=Label(root,text="")
Pscore=Label(root,text="0")
Cscore=Label(root,text="0")

#placements
title.grid(row=0,column=4)
winstatus.grid(row=1,column=4)
optionstxt.grid(row=2,column=0)
scoretxt.grid(row=4,column=0)
Pselect.grid(row=5,column=1)
Cselect.grid(row=6,column=1)
Pscore.grid(row=5,column=2)
Cscore.grid(row=6,column=2)

#buttons
rock=Button(root,text="rock",background="red",command=lambda:choose("rock"))
paper=Button(root,text="paper",background="grey",command=lambda:choose("paper"))
scissors=Button(root,text="scissors",background="blue",command=lambda:choose("scissors"))

root.mainloop()
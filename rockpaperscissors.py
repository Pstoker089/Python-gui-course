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
pcount=0
ccount=0

#functions
def choose(option):
    global whowon
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
    Pselect.config(text="Player's choice: " + option)
    Cselect.config(text="Computer's choice: " + cchoice)
    winstatus.config(text=whowon)
    print(option)
    print(whowon)
    score(whowon)

def score(whowon):
    global Pscore
    global Cscore
    global ccount
    global pcount
    if whowon=="TIE":
        pass
    elif whowon=="COMPUTER WINS":
        ccount+=1
    elif whowon=="PLAYER WINS":
        pcount+=1
    Pscore.config(text="player's score: " + str(pcount))
    Cscore.config(text="Computer's score: " + str(ccount))




#cosmetics
root.title("Rock papaer scissors")
title=Label(root,text="Rock Paper Scissors",font=font.Font(size=20),fg="grey")
winstatus=Label(root,text="",fg="green")
optionstxt=Label(root,text="Your options:",fg="grey")
scoretxt=Label(root,text="Scores:",fg="grey")
Pselect=Label(root,text="Player's choice: "+option)
Cselect=Label(root,text="Computer's choice: "+cchoice)
Pscore=Label(root,text=pcount)
Cscore=Label(root,text=ccount)



#buttons
rock=Button(root,text="rock",background="red",command=lambda:choose("rock"))
paper=Button(root,text="paper",background="grey",command=lambda:choose("paper"))
scissors=Button(root,text="scissors",background="blue",command=lambda:choose("scissors"))



#placements
title.grid(row=0,column=1,columnspan=4)
winstatus.grid(row=1,column=1,columnspan=4)
optionstxt.grid(row=2,column=0)
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
scissors.grid(row=2,column=3)
scoretxt.grid(row=5,column=0)
Pscore.grid(row=5,column=4,columnspan=2)
Cscore.grid(row=6,column=4,columnspan=2)
Pselect.grid(row=5,column=1,columnspan=2)
Cselect.grid(row=6,column=1,columnspan=2)





root.mainloop()
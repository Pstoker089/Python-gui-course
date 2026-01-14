#basics
from tkinter import *
import tkinter.font as font
import random
root=Tk()
root.geometry("150x150")

#variables
whowon=""
cchoice=""
choicelist=["heads","tails"]


#functions
def flip():
    global whowon
    cchoice=random.choice(choicelist) 
    if cchoice=="heads":
        whowon="Heads wins!"
        answer.config(text=whowon)
    else:
        whowon="Tails wins!"
        answer.config(text=whowon)

#cosmetics
question=Label(root,text="Heads or Tails?",font=font.Font(size=15))
answer=Label(root,text=whowon,font=font.Font(size=15))



#buttons
btn=Button(root,text="Flip",background="yellow",command=lambda:flip(),font=font.Font(size=15))



#placements
question.grid(row=0,column=1)
btn.grid(row=1,column=1)
answer.grid(row=2,column=1)






root.mainloop()
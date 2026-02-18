from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Tic tac toe")
root.geometry("200x150")
#variables
result=""
turn=1



#functions
def win():
    global result
    #horizontal results
    if (b1.cget('text')==b2.cget("text")==b3.cget("text")=="X"):
        result="player 1 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b1.cget('text')==b2.cget("text")==b3.cget("text")=="O"):
        result="player 2 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b4.cget('text')==b5.cget("text")==b6.cget("text")=="X"):
        result="player 1 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b4.cget('text')==b5.cget("text")==b6.cget("text")=="O"):
        result="player 2 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b7.cget('text')==b8.cget("text")==b9.cget("text")=="X"):
        result="player 1 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b7.cget('text')==b8.cget("text")==b9.cget("text")=="O"):
        result="player 2 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    #vertical lines
    elif (b1.cget('text')==b4.cget("text")==b7.cget("text")=="X"):
        result="player 1 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b1.cget('text')==b4.cget("text")==b7.cget("text")=="O"):
        result="player 2 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b2.cget('text')==b5.cget("text")==b8.cget("text")=="X"):
        result="player 1 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b2.cget('text')==b5.cget("text")==b8.cget("text")=="O"):
        result="player 2 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b3.cget('text')==b6.cget("text")==b9.cget("text")=="X"):
        result="player 1 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b3.cget('text')==b6.cget("text")==b9.cget("text")=="O"):
        result="player 2 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    #diagonal lines
    elif (b1.cget('text')==b5.cget("text")==b9.cget("text")=="X"):
        result="player 1 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b1.cget('text')==b5.cget("text")==b9.cget("text")=="O"):
        result="player 2 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b7.cget('text')==b5.cget("text")==b3.cget("text")=="X"):
        result="player 1 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    elif (b7.cget('text')==b5.cget("text")==b3.cget("text")=="O"):
        result="player 2 wins"
        messagebox.showinfo("result",str(result))
        root.destroy()
    
def b1click():
    global turn
    mytext=b1.cget("text")
    if mytext=="":
        if turn==1:
            b1.configure(text="X")
            turn=2
        else:
            b1.configure(text="0")
            turn=1
        label.configure(text="player"+str(turn)+"turn")
        win()

b1=Button(root,text="",width=5,command=b1click)
b1.grid(column=0,row=0,padx=5,pady=5)

def b2click():
    global turn
    mytext=b2.cget("text")
    if mytext=="":
        if turn==1:
            b2.configure(text="X")
            turn=2
        else:
            b2.configure(text="0")
            turn=1
        label.configure(text="player"+str(turn)+"turn")
        win()       

b2=Button(root,text="",width=5,command=b2click)
b2.grid(column=0,row=1,padx=5,pady=5)

def b3click():
    global turn
    mytext=b3.cget("text")
    if mytext=="":
        if turn==1:
            b3.configure(text="X")
            turn=2
        else:
            b3.configure(text="0")
            turn=1
        label.configure(text="player"+str(turn)+"turn")
        win()
    
b3=Button(root,text="",width=5,command=b3click)
b3.grid(column=0,row=2,padx=5,pady=5)

def b4click():
    global turn
    mytext=b4.cget("text")
    if mytext=="":
        if turn==1:
            b4.configure(text="X")
            turn=2
        else:
            b4.configure(text="0")
            turn=1
        label.configure(text="player"+str(turn)+"turn")
        win()

b4=Button(root,text="",width=5,command=b4click)
b4.grid(column=1,row=0,padx=5,pady=5)

def b5click():
    global turn
    mytext=b5.cget("text")
    if mytext=="":
        if turn==1:
            b5.configure(text="X")
            turn=2
        else:
            b5.configure(text="0")
            turn=1
        label.configure(text="player"+str(turn)+"turn")
        win()

b5=Button(root,text="",width=5,command=b5click)
b5.grid(column=1,row=1,padx=5,pady=5)

def b6click():
    global turn
    mytext=b6.cget("text")
    if mytext=="":
        if turn==1:
            b6.configure(text="X")
            turn=2
        else:
            b6.configure(text="0")
            turn=1
        label.configure(text="player"+str(turn)+"turn")
        win()

b6=Button(root,text="",width=5,command=b6click)
b6.grid(column=1,row=2,padx=5,pady=5)

def b7click():
    global turn
    mytext=b7.cget("text")
    if mytext=="":
        if turn==1:
            b7.configure(text="X")
            turn=2
        else:
            b7.configure(text="0")
            turn=1
        label.configure(text="player"+str(turn)+"turn")
        win()

b7=Button(root,text="",width=5,command=b7click)
b7.grid(column=2,row=0,padx=5,pady=5)

def b8click():
    global turn
    mytext=b8.cget("text")
    if mytext=="":
        if turn==1:
            b8.configure(text="X")
            turn=2
        else:
            b8.configure(text="0")
            turn=1
        label.configure(text="player"+str(turn)+"turn")
        win()

b8=Button(root,text="",width=5,command=b8click)
b8.grid(column=2,row=1,padx=5,pady=5)

def b9click():
    global turn
    mytext=b9.cget("text")
    if mytext=="":
        if turn==1:
            b9.configure(text="X")
            turn=2
        else:
            b9.configure(text="0")
            turn=1
        label.configure(text="player"+str(turn)+"turn")
        win()

b9=Button(root,text="",width=5,command=b9click)
b9.grid(column=2,row=2,padx=5,pady=5)

label=Label(root,text="player "+str(turn)+" turn")
label.grid(row=3,column=1,padx=10,pady=10)


#mainloop
root.mainloop()
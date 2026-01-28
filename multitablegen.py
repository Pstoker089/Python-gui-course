from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title="Mathematical table generator"

title=Label(root,text="Mathematical table")
numbrangetxt=Label(root,text="number range")


title.grid(row=0,column=0,columnspan=3,pady=25)
numbrangetxt.grid(column=0,row=1,padx=10)


number=IntVar()
numbox=Combobox(root,textvariable=number,width=5)
numbox["values"]=tuple(range(101))

numrange=IntVar()
r1=Radiobutton(root,text="10",variable=numrange,value=10)
r2=Radiobutton(root,text="20",variable=numrange,value=20)
r3=Radiobutton(root,text="30",variable=numrange,value=30)

numrange.set(10)

numbox.grid(column=1,row=1)
r1.grid(column=2,row=1)
r2.grid(column=2,row=2,padx=30)
r3.grid(column=2,row=3,padx=30)

def generate():
    tables=""
    for i in range(numrange.get()+1):
        tables+=str(number.get())+" X "+str(i)+" = " +str(number.get()*i)+"\n"
    table.configure(text=tables)




genbtn=Button(root,text="generate",command=generate)
table=Label(root,anchor="center")
genbtn.grid(row=4,column=1)
table.grid(row=5,column=1,pady=25)


root.mainloop()
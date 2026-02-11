#essentials 
from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.title("Memoriser")
root.config(width=800,height=700)

#functions
def openfile():
    global item
    fin=askopenfile(title="open file")
    if fin is not None:
        Listbox.delete(0,END)
        items=fin.readlines()
        for item in items:
            Listbox.insert(END,item.strip())

def savefile():
    fout=asksaveasfile(defaultextension=".txt")
    if fout is not None:
        for item in Listbox.get(0,END):
            print(item.strip(),file=fout)
        Listbox.delete(0,END)

def additem():
    Listbox.insert(END,item.get())
    item.delete(0,END) 

def deleteitem():
    index=Listbox.curselection()
    if index:
        Listbox.delete(index)

#buttons/placements
    # open, delete and save buttons/placements
fopen=Button(root,text="OPEN",command=openfile,width=15)
ldelete=Button(root,text="DELETE",command=deleteitem,width=15)
fsave=Button(root,text="SAVE",command=savefile,width=15)
fopen.pack(side=LEFT,padx=5,pady=5)
ldelete.pack(side=RIGHT,padx=5,pady=5)
fsave.pack(padx=5,pady=5)
    #add and item entry buttons/placements
ladd=Button(root,text="ADD",command=additem,width=15)
ladd.pack(padx=5,pady=5)
itement=Entry(root,width=35)
itement.pack(padx=5,pady=5)

#listbox creation
frame=Frame(root)
scrollbar=Scrollbar(frame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

listbox=Listbox(frame,width=20,yscrollcommand=scrollbar.set,bg="red")
for i in range(1,101):
    listbox.insert(END,"list"+str(i))
listbox.pack(side=LEFT,padx=5)
scrollbar.config(command=listbox.yview)
frame.pack(side=RIGHT)



#mainloop
root.mainloop()
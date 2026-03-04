from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Address book")
root.geometry("600x500")

#title
bookname=Label(root,text="My address book!",width=35)
bookname.grid(row=0,column=1,pady=10,columnspan=3)
#contact list / listbox
conlist=Listbox(root,height=15,width=30)
conlist.grid(row=2,column=0,columnspan=3,rowspan=5)
#contact info fields
namelab=Label(root,text="Name")
namelab.grid(row=3,column=3)
nameent=Entry(root)
nameent.grid(row=3,column=4)
addresslab=Label(root,text="Address")
addresslab.grid(row=4,column=3)
addressent=Entry(root)
addressent.grid(row=4,column=4)
emaillab=Label(root,text="Email")
emaillab.grid(row=5,column=3)
emailent=Entry(root)
emailent.grid(row=5,column=4)
bdaylab=Label(root,text="Birthday")
bdaylab.grid(row=6,column=3)
bdayent=Entry(root)
bdayent.grid(row=6,column=4)
phonelab=Label(root,text="Phone number").grid(row=7,column=3)
phoneent=Entry(root).grid(row=7,column=4)

#buttons (open, edit, delete and save)
editbtn=Button(root,text="Edit",bg="blue").grid(row=0,column=4)
delbtn=Button(root,text="Delete",bg="red").grid(row=0,column=5)
savebtn=Button(root,text="Save",bg="green").grid(row=0,column=6,padx=50)
opn=Button(root,text="open")
opn.grid(row=0,column=3,pady=10)

#functions
def openhoverfunc(e):
    opn["bg"]="red"

def closehoverfunc(p):
    opn["bg"]="grey"

opn.bind("<Enter>", openhoverfunc)
opn.bind("<Leave>", closehoverfunc)
    






root.mainloop()
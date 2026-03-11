from tkinter import *
#from tkinter.ttk import *

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
phoneent=Entry(root)
phoneent.grid(row=7,column=4)

#functions
 #add function
def add_contact():
    contact=nameent.get()+" | "+addressent.get()+" | " +phoneent.get()+ " | "+emailent.get()+ " | "+bdayent.get()
    conlist.insert(END,contact)
    nameent.delete(0,END)
    addressent.delete(0,END)
    phoneent.delete(0,END)
    emailent.delete(0,END)
    bdayent.delete(0,END)

 #delete function
def delete_contact():
    selected_contact=conlist.curselection()
    if selected_contact:
        conlist.delete(selected_contact[0])

 #edit function
def edit_contact():
    selected=conlist.curselection()
    if selected:
        index=selected[0]
        updated_contact=nameent.get()+" | "+addressent.get()+" | " +phoneent.get()+ " | "+emailent.get()+ " | "+bdayent.get()
        conlist.delete(index)
        conlist.insert(index,updated_contact)

 #save function
def save_contacts():
    with open("extention.txt",W) as file:
        contacts=conlist.get(0,END)
        for contact in contacts:
            file.write(contact +"\n")
    print("contact saved succesfully")

 #open function
def open_action():
    conlist.delete(0,END)
    try:
        with open("extention.txt","r") as file:
            for l in file:
                conlist.insert(END,l.strip())
    except FileNotFoundError:
        print("No saved contact found")



#buttons (open, edit, delete and save)
editbtn=Button(root,text="Edit",bg="blue",command=edit_contact)
editbtn.grid(row=0,column=4)
delbtn=Button(root,text="Delete",bg="red", command=delete_contact)
delbtn.grid(row=0,column=5)
savebtn=Button(root,text="Save",bg="green",command=save_contacts)
savebtn.grid(row=0,column=6,padx=50)
opn=Button(root,text="open",command=open_action)
opn.grid(row=1,column=3,pady=10)
add_button=Button(root,text="Add Contact", command=add_contact)
add_button.grid(row=1, column=4, padx=10)

#cosmetic functions
#def openhoverfunc(e):
#    opn["bg"]="red"
#def closehoverfunc(p):
#    opn["bg"]="white"
#opn.bind("<Enter>", openhoverfunc)
#opn.bind("<Leave>", closehoverfunc)


#add_contact()


root.mainloop()
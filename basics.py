from tkinter import *

#buttons

"""root=Tk()
root.geometry("100x100")

btn=Button(root,text="click me",background="white",command=root.destroy)
btn.pack(side='top')


root.mainloop()"""


#labels and entries

root=Tk()
root.geometry("450x300")
root.config(background="pink")
root.title("Login")

user=Label(root,text="Username :",background="pink")
user.place(x=30, y=40)
username=Entry(root,width=50)
username.place(x=100, y=40)

pas=Label(root,text="Password :",background="pink").place(x=30, y=80)
password=Entry(root,width=50).place(x=100, y=80)

login=Button(root, text="Login", background="white",command=root.destroy).place(x=80, y=120)




root.mainloop()
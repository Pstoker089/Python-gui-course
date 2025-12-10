from tkinter import *
root=Tk()
root.geometry("670x100")

def convert():
    weight=float(entent.get())
    gramcalc=weight*1000
    poundcalc=weight*2.205
    ouncecalc=weight*35.274
    gramconv.insert(END,gramcalc)
    poundconv.insert(END,poundcalc)
    ounceconv.insert(END,ouncecalc)



enttext=Label(root,text="Enter the weight in Kg")
entent=Entry(root,width=50)
conv=Button(root,text="convert",background="white",command=convert)
gramtxt=Label(root,text="Grams")
poundtxt=Label(root,text="Pounds")
ouncetxt=Label(root,text="Ounces")
gramconv=Text(root,height=1,width=20)
poundconv=Text(root,height=1,width=20)
ounceconv=Text(root,height=1,width=20)

enttext.grid(row=0,column=0)
entent.grid(row=0,column=1)
conv.grid(row=0,column=2)
gramtxt.grid(row=1,column=0)
poundtxt.grid(row=1,column=1)
ouncetxt.grid(row=1,column=2)
gramconv.grid(row=2,column=0)
poundconv.grid(row=2,column=1)
ounceconv.grid(row=2,column=2)









root.mainloop()
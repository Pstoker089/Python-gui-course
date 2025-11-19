from tkinter import *
import calendar
root=Tk()
root.geometry("350x140")
root.title("Calender")

def cal():
    rooty=Tk()
    rooty.geometry("510x600")
    rooty.title("Calender")
    year=int(yearchoice.get())
    calen=calendar.calendar(year)
    print(calen)
    #entirecal=Label(rooty,text=calen)
    #entirecal.grid(row=5,column=1)
    text_area = Text(rooty, font=("Consolas", 10),width=700, height=500)
    text_area.insert(INSERT, calen)
    text_area.grid(row=4, column=3)
    rooty.mainloop()


title=Label(root,text="Calender",background="white",font=("times", 28, 'bold'))
yearchoicetext=Label(root,text="Enter a year",background="green")
yearchoice=Entry(root,width=50)
select=Button(root,width=25,text="select this year?",bg="red",command=cal)
exit=Button(root,command=exit,width=5,text="exit",bg="red")

title.pack()
yearchoice.pack()
yearchoicetext.pack()
select.pack()
exit.pack()
root.mainloop()
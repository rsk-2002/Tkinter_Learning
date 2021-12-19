from tkinter import *
def getVals():
    with open('records.txt','a')as f:
        text = f"{namevalue.get()}-{agevalue.get()}\n"
        f.write(text)
        exit()
root = Tk()
root.geometry('700x400')
name = Label(root,text='Enter Your Name')
age = Label(root,text='Enter Your Age')
name.grid()
age.grid(row=1)
namevalue = StringVar()
agevalue = IntVar()
nameEnter = Entry(root,textvariable=namevalue)
ageEnter = Entry(root,textvariable=agevalue)
nameEnter.grid(row=0,column=1)
ageEnter.grid(row=1,column=1)
Button(text="Join",command=getVals).grid(row=2,column=1)
root.mainloop()
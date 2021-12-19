from tkinter import *

def getVals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The password of user is {passvalue.get()}")
root = Tk()
root.geometry('700x400')

user = Label(root,text='Username')
password = Label(root,text='Password')
user.grid()
password.grid(row=1)

# Variable in tkinter 
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable=uservalue)
passentry = Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getVals).grid(row=2,column=1)

root.mainloop()
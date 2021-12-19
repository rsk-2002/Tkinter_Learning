from tkinter import *

root = Tk()

def getVals():
    print("It works")
root.geometry('600x400')
# heading
Label(root, text='Welcome to Ravi Travels',pady=15,font='comicsans 13 bold').grid(row=0,column=3)

name = Label(root,text='Name')
phone = Label(root,text='Phone')

name.grid(row=1,column=2)
phone.grid(row=2,column=2)

namevalue = StringVar()
phonevalue = StringVar()

# Entries for our form 
nameentry = Entry(root,textvariable=namevalue)
phoneentry = Entry(root,textvariable=phonevalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
Button(text="Submit",command=getVals).grid(row=3,column=3)
root.mainloop()
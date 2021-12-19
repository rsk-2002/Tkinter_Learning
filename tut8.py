from tkinter import *

root = Tk()
root.geometry('700x300')

f1 = Frame(root,bg='gray',borderwidth=4,relief=RIDGE)
f1.pack(side=LEFT,fill="y")

f2 = Frame(root,bg='black',borderwidth=4,relief=RIDGE)
f2.pack(side=TOP,fill="x")

l = Label(f1,text="Project Tkinter - Pycharm")
l.pack(pady=100,padx=400)

l2 = Label(f2,text="Welcome to Sublime text")
l2.pack(pady=40,padx=30)

root.mainloop()
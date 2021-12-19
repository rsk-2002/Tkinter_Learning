from tkinter import *
root = Tk()
root.geometry('600x400')
def morning():
    print("Good Morning")
def evening():
    print("Good evening")
def afternoon():
    print("Good Afternoon")
f1 = Frame(root,borderwidth=4,bg='coral',relief=RIDGE)
f1.pack(side=TOP,anchor='nw')
b1 = Button(f1,text="Afternoon Time",command=afternoon)
b1.pack(side=LEFT)
b2 = Button(f1,text="Evening Time",command=evening)
b2.pack(side=LEFT)
b3 = Button(f1,text="Morning Time",command=morning)
b3.pack(side=LEFT)
root.mainloop()
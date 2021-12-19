from tkinter import *

root = Tk()
root.geometry('700x300')

def hello():
    print("Hello tkinter button")
def name():
    print("Name is Ravi")

frame = Frame(root, borderwidth=6,bg='purple',relief=SUNKEN)
frame.pack(side=LEFT,anchor='nw')

b1 = Button(frame,fg='red',text='Print Now',command=hello)
b1.pack(side=LEFT,padx=23)

b2 = Button(frame,fg='red',text='Tell me name Now',command=name)
b2.pack(side=LEFT,padx=23)

b3 = Button(frame,fg='red',text='Print Now')
b3.pack(side=LEFT,padx=23)

b4 = Button(frame,fg='red',text='Print Now')
b4.pack(side=LEFT,padx=23)


root.mainloop()
from tkinter import *
i = 0
def additem():
    global i
    i+=1
    lbx.insert(ACTIVE,f"{i} item of our listbox")
i=0
root = Tk()
root.geometry('600x400')
root.title('Listbox in tkinter')

lbx = Listbox(root)
lbx.pack()

lbx.insert(END,"First item of our listbox")

Button(root,text="Add Item",command=additem).pack()


root.mainloop()
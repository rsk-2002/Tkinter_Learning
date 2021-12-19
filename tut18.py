from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('733x400')
root.title('My Title')

def myfunc():
    print('I am function with a print statement')

def help():
    print("I will help you")
    tmsg.showinfo("This","Ravi will help you with this GUI")

def rate():
    print("Rate us")
    a = tmsg.askquestion("Was your experience good?","Was your experience good?")
    if a=="yes":
        msg = "Rate us on appstore"
    else:
        msg = "Tell us what went wrong?"
    tmsg.showinfo("Exeperience",msg)

def divya():
    ans = tmsg.askretrycancel("Divya se dosti karlo","Sorry divya nahi banegi aapaki dost")
    if ans:
        print("Retry karne pe bhi kuch nahi hoga")
    else:
        print("Bahut badiya bhai cancel kar diya warna pitte")


mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="New Project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save As",command=myfunc)
m1.add_command(label="Print",command=myfunc)
mainmenu.add_cascade(label="File",menu=m1)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Undo",command=myfunc)
mainmenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)
m3.add_command(label="Be friend Divya",command=divya)
mainmenu.add_cascade(label="Help",menu=m3)

root.config(menu=mainmenu)




root.mainloop()
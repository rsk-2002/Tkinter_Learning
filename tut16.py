from tkinter import *
def setVals():
    val = f"{widthvalue.get()}x{heightvalue.get()}"
    root.geometry(val)
root = Tk()
root.geometry('400x300')
width = Label(root,text='Enter Width')
height = Label(root,text='Enter Height')
width.grid()
height.grid(row=1)
widthvalue = StringVar()
heightvalue = StringVar()
widthE = Entry(root,textvariable=widthvalue)
heightE = Entry(root,textvariable=heightvalue)
widthE.grid(row=0,column=1)
heightE.grid(row=1,column=1)
Button(text="Apply",command=setVals).grid(row=2,column=1)
root.mainloop()
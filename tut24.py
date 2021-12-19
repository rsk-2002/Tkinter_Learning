from tkinter import *

def upload():
    statusvar.set('Busy...')
    statusbar.update()
    import time 
    time.sleep(2)
    statusvar.set('on the way...')

root = Tk()
root.geometry('600x400')
root.title('Status bar in tkinter')

statusvar = StringVar()
statusvar.set("on the way...")
statusbar = Label(root, textvariable=statusvar, bd=1, relief=SUNKEN, anchor=W)

statusbar.pack(side=BOTTOM, fill=X)
Button(root,text="Upload",command=upload).pack()

root.mainloop()
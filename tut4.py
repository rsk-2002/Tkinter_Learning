from tkinter import *

ravi_root = Tk()

#with X height 

ravi_root.geometry("444x234")
# with , height 
ravi_root.minsize(300,100)
ravi_root.maxsize(800,600)

aman = Label(text = "I am a good boy and this is his GUI")
aman.pack()

ravi_root.mainloop()
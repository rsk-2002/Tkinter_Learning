from tkinter import *
import tkinter.messagebox as tmsg

def getdollars():
    print(f"${myslider2.get()}")
    tmsg.showinfo("This",f"${myslider2.get()}")
root = Tk()
root.geometry('600x400')
root.title('Slider in Tkinter')

# myslider = Scale(root,from_=0,to=100)
# myslider.pack()
Label(root,text="How many dollars do you want?").pack()

myslider2 = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(30)
myslider2.pack()
Button(root,text="Get dollars!",command=getdollars).pack()

root.mainloop()
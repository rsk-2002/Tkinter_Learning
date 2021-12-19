from tkinter import *
def rateus():
    rating = f"{myslider2.get()}\n"
    with open('record.txt','a') as f:
        f.write(str(rating))
root = Tk()
root.geometry('600x400')
root.title('Slider in Tkinter')
Label(root,text="How many stars we deserve?").pack()
myslider2 = Scale(root,from_=0,to=5,orient=HORIZONTAL)
myslider2.set(4)
myslider2.pack()
Button(root,text="Please Rate us!",command=rateus).pack()
root.mainloop()
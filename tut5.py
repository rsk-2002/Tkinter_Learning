from tkinter import *
from PIL import Image,ImageTk

adarsh_root = Tk()


adarsh_root.geometry("900x420")
photo = PhotoImage(file='2.png')
varun_label = Label(image=photo)
varun_label.pack()


# for jpg image 
# image = Image.open('1.jpg')
# photo = ImageTk.PhotoImage(image)
# varun_label = Label(image=photo)
# varun_label.pack()


adarsh_root.mainloop()
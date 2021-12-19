from tkinter import *
from PIL import Image,ImageTk


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x400')

    def Image(self):
        self.image = PhotoImage('2.png')
        self.label = Label(image=self.image)
        self.label.pack()

#     image = Image.open('1.jpg')
# photo = ImageTk.PhotoImage(image)
# varun_label = Label(image=photo)
# varun_label.pack()    

if __name__=='__main__':
    window = GUI()
    window.Image()
    window.mainloop()
from tkinter import *

def ravi(event):
    print(f"You clicked on this button at {event.x},{event.y}")
root = Tk()
root.title('Events in Tkinter')
root.geometry('700x300')

widget = Button(root,text='Click me please')
widget.pack()

widget.bind('<Button-1>',ravi)
widget.bind('<Double-1>',quit)
root.mainloop()
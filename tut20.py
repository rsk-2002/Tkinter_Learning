from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("Order Receieved",f"We have received your order {var.get()}")
root = Tk()
root.geometry('600x400')
root.title('Radio button tutorial')

# var = IntVar()
var = StringVar()
var.set("Dosa")
Label(root, text = "What would you like to have sir?",font="lucida 20 bold",justify=LEFT,pady=14).pack()

radio = Radiobutton(root, text = "Dosa",padx=10,variable=var, value="Dosa").pack(anchor='w')
radio = Radiobutton(root, text = "Idly",padx=10,variable=var, value="Idly").pack(anchor='w')
radio = Radiobutton(root, text = "Paratha",padx=10,variable=var, value="Paratha").pack(anchor='w')
radio = Radiobutton(root, text = "Samosa",padx=10,variable=var, value="Samosa").pack(anchor='w')

Button(text="Order Now",command=order,padx=10).pack(anchor='w')

root.mainloop()
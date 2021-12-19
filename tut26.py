from tkinter import * 
root = Tk()
root.geometry('700x400')
root.title("rsk - Title of my GUI")
root.wm_iconbitmap('1.ico')
root.configure(background="gray")


width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")
Button(root,text="Close",command=root.destroy).pack()
root.mainloop()
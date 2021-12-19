from tkinter import *

def click(event):
    global scValue
    text = event.widget.cget("text")
    if text =="=":
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            try:
                value = eval(scValue.get())
            except Exception as e:
                print(e)
                value = "Error"

        scValue.set(value)
        screen.update()
    elif text =="C":
        scValue.set("")
        screen.update()
    else:
        scValue.set(scValue.get()+text)
        screen.update()

    
root = Tk()
root.geometry('350x450')
root.title("Calculator In Tkinter")
root.wm_iconbitmap('1.ico')
root.configure(background="gray")


scValue = StringVar()
scValue.set("")

screen = Entry(root,textvar = scValue,font="Ariel 18")
screen.pack(fill=X,ipadx=25,padx=10,pady=10)


fontValue = StringVar()
fontValue.set("lucida 35 bold")

# ipadX = IntVar()
# ipadX.set(10)

# ipadY = IntVar()
# ipadY.set(8)

f1 = Frame(root,bg="lightslategrey")
b = Button(f1,text="7",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="8",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="9",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="C",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f1.pack()


f1 = Frame(root,bg="lightslategrey")
b = Button(f1,text="4",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="5",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="6",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="+",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f1.pack()


f1 = Frame(root,bg="lightslategrey")
b = Button(f1,text="1",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="2",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="3",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="-",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f1.pack()

f1 = Frame(root,bg="lightslategrey")
b = Button(f1,text="0",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="=",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="/",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="*",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f1.pack()


f1 = Frame(root,bg="lightslategrey")
b = Button(f1,text="%",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text=".",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text="(",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f1,text=")",padx=10,pady=8,font=fontValue)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f1.pack()


root.mainloop()
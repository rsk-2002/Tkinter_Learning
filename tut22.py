from tkinter import *

root = Tk()
root.geometry('700x400')
root.title('Scrollbar in tkinter')

# For connecting scrollbar to a widget
# 1.widget(yscrollcommand = scrollbar.set)
# scrollbar.config(command=widget.YView)

sc = Scrollbar(root)
sc.pack(side=RIGHT,fill=Y)

# listbox = Listbox(root,yscrollcommand = sc.set)
# for i in range(344):
#     listbox.insert(END,f"Item {i}")

text = Text(root,yscrollcommand = sc.set)
text.pack(fill=BOTH)

# listbox.pack(fill=BOTH,padx=22)
# sc.config(command=listbox.yview)
sc.config(command=text.yview)

root.mainloop()
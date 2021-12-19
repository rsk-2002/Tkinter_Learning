from tkinter import *
import os

root = Tk()
root.geometry("744x433")
root.title("My GUI with Harry ")


# text - adds the text
# bg - background
# fg - foreground
# 1. font - sets the font font=('cascadia code',15,"bold")
# 2. font="verdana 15 bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text = '''Space Exploration Technologies Corp. (SpaceX) is an \nAmerican aerospace manufacturer, space transportation services and \ncommunications corporation headquartered in Hawthorne, California. SpaceX was \nfounded in 2002 by Elon Musk with the goal of reducing space transportation \ncosts to enable the colonization of Mars. SpaceX manufactures the Falcon 9 and \nFalcon Heavy launch vehicles, several rocket engines, Dragon cargo, crew \nspacecraft and Starlink communications satellites.''',bg = "red",fg="white",padx=24,pady=24,font="verdana 15 bold",borderwidth=3,relief=SUNKEN)

# Important pack options 
# anchor = nw
# side - top,bottom,left,right
# fill
# padx
# pady
# title_label.pack(side=BOTTOM,anchor="nw",fill=X)
title_label.pack(side=LEFT,fill=Y,padx=23,pady=34)

title_label.pack()


root.mainloop()
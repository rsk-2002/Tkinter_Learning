from tkinter import *

root = Tk()

def getvals():
    print("Submitting Form")
    
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}")
    # print(f"{namevalue.get(),phonevalue.get()}\n")
    with open('record.txt','a')as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n")
root.geometry('600x400')
# heading
Label(root, text='Welcome to Ravi Travels',pady=15,font='comicsans 13 bold').grid(row=0,column=3)

# text for our form 
name = Label(root,text='Name')
phone = Label(root,text='Phone')
gender = Label(root,text='Gender')
emergency = Label(root,text='Emergency mode')
paymentmode = Label(root,text='Payment mode')

# pack text for our form 
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

# tkinter variable for storing values 
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# Entries for our form 
nameentry = Entry(root,textvariable=namevalue)
phoneentry = Entry(root,textvariable=phonevalue)
genderentry = Entry(root,textvariable=gendervalue)
emergencyentry = Entry(root,textvariable=emergencyvalue)
paymentmodeentry = Entry(root,textvariable=paymentmodevalue)

# packing the enteries 
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

# checkbox & packing it
foodservice = Checkbutton(text='Want to get your meals?',variable=foodservicevalue)
foodservice.grid(row=6,column=3)

# button and packing it and assign it a command
Button(text='Submit to Ravi travels',command=getvals).grid(row=7,column=3)
root.mainloop()
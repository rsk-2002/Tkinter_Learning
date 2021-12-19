from tkinter import *
from PIL import ImageTk,Image

def every_100(text):
    final_text = ""
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="\n"
    return final_text

root = Tk()
root.title('Apna Akhabaar')
root.geometry('1000x500')

texts = []
photos = []
for i in range(0,3):
    with open(f"{i+1}.txt",'r') as f:
        text = f.read()
        texts.append(every_100(text))
    
    image = Image.open(f"{i+1}.png")
    # TODO: resize these images
    image=image.resize((225,164),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))


f0 = Frame(root,width=800,height=70)
Label(f0,text='codewithharry News',font='lucida 33 bold').pack()
Label(f0,text='January 19, 2050',font='lucida 13 bold').pack()
f0.pack()

f1 = Frame(root,width=300,height=400)
Label(f1,text=texts[0],padx=22,pady=34).pack(side='left')
Label(f1,image=photos[0],anchor="e").pack(side='left')
f1.pack(anchor="w")

f2 = Frame(root,width=300,height=400)
Label(f2,text=texts[1],padx=22,pady=34).pack(side='left')
Label(f2,image=photos[1],anchor="e").pack(side='left')
f2.pack(anchor="w")

f3 = Frame(root,width=300,height=400)
Label(f3,text=texts[2],padx=22,pady=34).pack(side='left')
Label(f3,image=photos[2],anchor="e").pack(side='left')
f3.pack(anchor="w")

root.mainloop()
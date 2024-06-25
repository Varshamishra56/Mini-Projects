
#RadioButton
from tkinter import *
root=Tk()
lab=Label(root)
lab.pack()
val=IntVar()
def change():
    lab.config(text=str(val.get()))

Radiobutton(root,text="male",variable=val,value=1,command=change).pack()
Radiobutton(root,text="female",variable=val,value=2,command=change).pack()
root.mainloop() 
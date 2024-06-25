#Button
from tkinter import *
root=Tk()
root.geometry("555x555")
lab=Label(root)
val=IntVar
def hello():
    return lab.config(text=str(val.get("Hi How are you??")))

b1=Button(root,fg="black",text="MALE",textvariable=val,command=hello)
b1.pack()
b1=Button(root,fg="black",text="FEMALE")
b1.pack()
b1=Button(root,fg="black",text="OTHERS")
b1.pack()
b1=Button(root,fg="black",text="SELECT")
b1.pack()
root.mainloop()

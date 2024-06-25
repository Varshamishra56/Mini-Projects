#WindowsUpdate
from tkinter import *
root=Tk()
root.geometry("344x344")

def update():
    print("updating the GUI")
    root.geometry(f"{width.get()}x{height.get()}")
width=StringVar()
height=StringVar()
Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()
Button(root,text="Apply changes",command=update).pack()

root.mainloop()
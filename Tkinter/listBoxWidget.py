#ListBoxWidget
from tkinter import *
def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1
i=0
root=Tk()
root.geometry("455x433")
root.title("Listbox")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"first Itm of the list box")

Button(root,text="Add item",command=add).pack()
root.mainloop()
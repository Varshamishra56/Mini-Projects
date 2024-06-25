#StatusBar
from tkinter import *

def upload():
    statusvar.set("BUSY...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready now")
root=Tk()
root.geometry("566x566")
root.title("status bar")

statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="upload",command=upload).pack()

root.mainloop()
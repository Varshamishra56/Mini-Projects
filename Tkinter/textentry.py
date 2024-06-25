#GridPack
from tkinter import *
def getvalue():
    print("the value of the username is ",userentry.get())
    print("the value of the password is ",passentry.get())

root =Tk()
root.geometry("655x655")
user=Label(root,text="Username")
password=Label(root,text="password")
user.grid()
password.grid(row=1)
uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=StringVar())
passentry=Entry(root,textvariable=StringVar())
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="submit",command=getvalue).grid(row=9)

root.mainloop()
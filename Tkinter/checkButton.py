#CheckButton
from tkinter import *

root=Tk()
def getvals():
    print("it works")
root.geometry("655x655")
Label(root,text="Welcome to AI Travels",font="comicsansms 15 bold",pady=15).grid(row=0,column=3)

name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="gender")
emergency=Label(root,text="emergency contact")
paymentmode=Label(root,text="Payment mode")

name.grid(row=3,column=2)
phone.grid(row=4,column=2)
gender.grid(row=5,column=2)
emergency.grid(row=6,column=2)
paymentmode.grid(row=7,column=2)

nameentry=Entry(root,textvariable=StringVar())
phoneentry=Entry(root,textvariable=StringVar())
genderentry=Entry(root,textvariable=StringVar())
emergencyentry=Entry(root,textvariable=StringVar())
paymentmodeentry=Entry(root,textvariable=StringVar())

nameentry.grid(row=3,column=4)
phoneentry.grid(row=4,column=4)
genderentry.grid(row=5,column=4)
emergencyentry.grid(row=6,column=4)
paymentmodeentry.grid(row=7,column=4)

foodservice=Checkbutton(text="do you want to prebook your meal",variable=StringVar())
foodservice.grid(row=8,column=3)

Button(text="submit to AI travels",command=getvals).grid(row=10,column=2)
root.mainloop()
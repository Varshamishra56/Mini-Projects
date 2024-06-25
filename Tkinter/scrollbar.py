# SCrollBar
from tkinter import *
root=Tk()
root.geometry("455x455")
root.title("Scroll Bar")
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(root,yscrollcommand=scrollbar.set)
scrollbar.pack(fill="both",padx=22)
scrollbar.config(command=listbox.yview)
for i in range(100):
    listbox.insert(END,f"item {i}")
listbox.pack()

# text=Text(root,yscrollcommand=scrollbar.set)
# text.pack(fill=BOTH)
# scrollbar.config(command=text.yview)

root.mainloop()
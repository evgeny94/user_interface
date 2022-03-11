from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Radio')
#root.iconbitmap('images/icon.ico')

r = IntVar()
r.set("0")
#555
def myDelete():
    myLabel.pack_forget()

def clicked(value):
    global myLabel

    myDelete()
    myLabel = Label(root, text=value)
    myLabel.pack()


Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda : clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda : clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

root.mainloop()
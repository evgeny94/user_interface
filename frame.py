from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Frame')
root.iconbitmap('images/icon.ico')

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

myLabel = Label(frame, text="My Label is Here")
myLabel.pack()

b = Button(frame, text="Click Here")
b.pack()


root.mainloop()
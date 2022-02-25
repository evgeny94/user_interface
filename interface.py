from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name Is Evgeny Musatov")


# Show on the screen(pack)
#myLabel1.pack()
#myLabel2.pack()

# Show on the screen(grid)
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

def myClick():
    myAnswer = e.get()
    myLabel = Label(root, text=myAnswer)
    myLabel.grid()

# Creating a button     # (state=DISABLED)  # (padx=50, pady=50)  #(fg="blue", bg="white")
myButton = Button(root, text="Click Me!", command=myClick)
myButton.grid(row=2, column=2)

# Input Box
e = Entry()
e.grid(row=4, column=4)
e.insert(0, "Enter Your Name:")

root.mainloop()
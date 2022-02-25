from tkinter import *

root = Tk()
root.title("Simple Calculator")

# Input Box
e = Entry(root, width=35, borderwidth=2)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)

def button_add():
    a = e.get()
    global num
    global math
    math = "add"
    num = int(a)
    e.delete(0, END)

def button_minus():
    a = e.get()
    global num
    global math
    math = "sub"
    num = int(a)
    e.delete(0, END)

def button_multiply():
    a = e.get()
    global num
    global math
    math = "mul"
    num = int(a)
    e.delete(0, END)


def button_divide():
    a = e.get()
    global num
    global math
    math = "div"
    num = int(a)
    e.delete(0, END)


def button_equal():
    b = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, num + int(b))
    elif math == "sub":
        e.insert(0, num - int(b))
    elif math == "mul":
        e.insert(0, num * int(b))
    elif math == "div":
        e.insert(0, num / int(b))

# Creating a button     # (state=DISABLED)  # (padx=50, pady=50)  #(fg="blue", bg="white")
# 7
button_7 = Button(root, text="7", command=lambda : button_click(7), padx=40, pady=20)
button_7.grid(row=1, column=0)
# 8
button_8 = Button(root, text="8", command=lambda : button_click(8), padx=40, pady=20)
button_8.grid(row=1, column=1)
# 9
button_9 = Button(root, text="9", command=lambda : button_click(9), padx=40, pady=20)
button_9.grid(row=1, column=2)
# 4
button_4 = Button(root, text="4", command=lambda : button_click(4), padx=40, pady=20)
button_4.grid(row=2, column=0)
# 5
button_5 = Button(root, text="5", command=lambda : button_click(5), padx=40, pady=20)
button_5.grid(row=2, column=1)
# 6
button_6 = Button(root, text="6", command=lambda : button_click(6), padx=40, pady=20)
button_6.grid(row=2, column=2)
# 1
button_1 = Button(root, text="1", command=lambda : button_click(1), padx=40, pady=20)
button_1.grid(row=3, column=0)
# 2
button_2 = Button(root, text="2", command=lambda : button_click(2), padx=40, pady=20)
button_2.grid(row=3, column=1)
# 3
button_3 = Button(root, text="3", command=lambda : button_click(3), padx=40, pady=20)
button_3.grid(row=3, column=2)
# 0
button_0 = Button(root, text="0", command=lambda : button_click(0), padx=40, pady=20)
button_0.grid(row=4, column=0)
# Clear
button_Clear = Button(root, text="Clear", command=button_clear, padx=77, pady=20)
button_Clear.grid(row=4, column=1, columnspan=2)
# +
button_Plus = Button(root, text="+", command=button_add, padx=39, pady=20)
button_Plus.grid(row=5, column=0)
# =
button_Equal = Button(root, text="=", command=button_equal, padx=86, pady=20)
button_Equal.grid(row=5, column=1, columnspan=2)
# -
button_Minus = Button(root, text="-", command=button_minus, padx=41, pady=20)
button_Minus.grid(row=6, column=0)
# *
button_Multiply = Button(root, text="*", command=button_multiply, padx=40, pady=20)
button_Multiply.grid(row=6, column=1)
# /
button_Divide = Button(root, text="/", command=button_divide, padx=40, pady=20)
button_Divide.grid(row=6, column=2)

root.mainloop()
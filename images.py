from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Images')
root.iconbitmap('images/icon.ico')

my_img0 = ImageTk.PhotoImage(Image.open('images/image1.jfif'))
my_img1 = ImageTk.PhotoImage(Image.open('images/image2.jfif'))
my_img2 = ImageTk.PhotoImage(Image.open('images/image3.jfif'))
my_img3 = ImageTk.PhotoImage(Image.open('images/image4.jfif'))
my_img4 = ImageTk.PhotoImage(Image.open('images/image5.jfif'))

image_list = [my_img0, my_img1, my_img2, my_img3, my_img4]

status = Label(root, text="Image " + "1" + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img0)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text="Right", command=lambda: forward(image_number+1))
    button_backward = Button(root, text="Left", command=lambda: backward(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text="Right", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def backward(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text="Right", command=lambda: forward(image_number+1))
    button_backward = Button(root, text="Left", command=lambda: backward(image_number-1))

    if image_number == 0:
        button_backward = Button(root, text="Left", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back = Button(root, text="Left", command=backward, state=DISABLED)
button_back.grid(row=1, column=0)

button_next = Button(root, text="Right", command=lambda : forward(2))
button_next.grid(row=1, column=2)

button_Quit = Button(root, text="Exit Program", command=root.quit)
button_Quit.grid(row=1, column=1, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)



root.mainloop()
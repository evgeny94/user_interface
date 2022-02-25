from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('User Interface')
root.iconbitmap('images/icon.ico')

screen_width = int(int(root.winfo_screenwidth())*0.92)
screen_height = int(int(root.winfo_screenheight())*0.9)
print(screen_width)
print(screen_height)
screen_width1 = root.winfo_screenwidth()
screen_height1 = root.winfo_screenheight()
geometry = str(screen_width) + "x" + str(screen_height)

root.geometry(geometry)

palm_img = Image.open('images/palm.jpg')

#Resize the Image using resize method
resized_image = palm_img.resize((screen_width, screen_height), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
palm_img = ImageTk.PhotoImage(Image.open('images/palm.jpg'))
# Grid Configurations
Grid.rowconfigure(root, index=0, weight=2)
Grid.columnconfigure(root, index=0, weight=2)
#Grid.rowconfigure(root, index=1, weight=1)

##--------------------------Left Side-------------------------##

# Frame Creation
frame = LabelFrame(root, text="Picture")
frame.grid(row=0, column=0, sticky="nsew")

# Frame Configuration
frame.rowconfigure(index=0, weight=1)
frame.columnconfigure(index=0, weight=1)

my_label = Label(frame, image=new_image)
my_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

##--------------------------Right Side-------------------------##

# Frame Creation
frame_right = LabelFrame(root, text="Information Section")
frame_right.grid(row=0, column=1, sticky="nsew")

# Frame Configuration
frame_right.rowconfigure(index=0, weight=0)
frame_right.columnconfigure(index=0, weight=0)
frame_right.rowconfigure(index=1, weight=0)
frame_right.columnconfigure(index=1, weight=0)
frame_right.rowconfigure(index=2, weight=0)
frame_right.rowconfigure(index=3, weight=0)

option_label = Label(frame_right, text="Choose an option for operation:")
option_label.grid(row=0, column=0, sticky="w")

# Radio Buttons
r = StringVar()
r.set("None")

def myDelete():
    selectedRadio.grid_forget()

def clicked(value):
    global selectedRadio
    global ge
    global b_submit
    global b_clear

    myDelete()
    if value == "Input of amount":
        ge = Entry(frame_right, width=28, borderwidth=2)
        ge.grid(row=3, column=0, sticky="w", padx=5, pady=10)

        b_submit = Button(frame_right, text="Submit", command=submit_entry)
        b_submit.grid(row=3, column=0, sticky="e", padx=10, pady=10)

        b_clear = Button(frame_right, text="Clear", command=clear_entry)
        b_clear.grid(row=3, column=1, sticky="w")
    else:
        ge = Entry(frame_right, width=28, borderwidth=2, state=DISABLED)
        ge.grid(row=3, column=0, sticky="w", padx=5, pady=10)

        b_submit = Button(frame_right, text="Submit", command=submit_entry, state=DISABLED)
        b_submit.grid(row=3, column=0, sticky="e", padx=10, pady=10)

        b_clear = Button(frame_right, text="Clear", command=clear_entry, state=DISABLED)
        b_clear.grid(row=3, column=1, sticky="w")

    selectedRadio = Label(frame_right, text="Option Selected: " + str(value))
    selectedRadio.grid(row=4, column=0, columnspan=2)

def clear_entry():
    ge.delete(0, END)

def submit_entry():
    ge.delete(0, END)

Radiobutton(frame_right, text="Manual marking on the image", variable=r, value="Manual marking", command=lambda : clicked(r.get())).grid(row=1, column=0, sticky="w")
Radiobutton(frame_right, text="Enter input for the amount that will remain", variable=r, value="Input of amount", command=lambda : clicked(r.get())).grid(row=2, column=0, sticky="w")

# Input Box
ge = Entry(frame_right, width=28, borderwidth=2, state=DISABLED)
ge.grid(row=3, column=0, sticky="w", padx=5, pady=10)

b_submit = Button(frame_right, text="Submit", command=submit_entry, state=DISABLED)
b_submit.grid(row=3, column=0, sticky="e", padx=10, pady=10)

b_clear = Button(frame_right, text="Clear", command=clear_entry, state=DISABLED)
b_clear.grid(row=3, column=1, sticky="w")

selectedRadio = Label(frame_right, text="Option Selected: " + str(r.get()))
selectedRadio.grid(row=4, column=0, columnspan=2)



#while TRUE:
#    root.update()
#    width = frame.winfo_width()
#    height = frame.winfo_height()
#    print("The width of the label is:", width,height, "pixels")

#b = Button(frame, text="Click Here")
#b.grid(row=1, column=0, sticky="nsew")


root.mainloop()
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
frame_right.rowconfigure(index=0, weight=1)
frame_right.columnconfigure(index=0, weight=1)

my_label = Label(frame_right, text="Information Section")
my_label.grid(row=0, column=0, sticky="nsew")


while TRUE:
    root.update()
    width = frame.winfo_width()
    height = frame.winfo_height()
    print("The width of the label is:", width,height, "pixels")

#b = Button(frame, text="Click Here")
#b.grid(row=1, column=0, sticky="nsew")


root.mainloop()
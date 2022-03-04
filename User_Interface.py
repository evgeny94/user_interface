import random
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

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
#palm_img = ImageTk.PhotoImage(Image.open('images/palm.jpg'))  not sure why it's here
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

##--------------------------Right Top Frame-------------------------##

top_right_frame = LabelFrame(frame_right ,text="Assessmention Section" )
top_right_frame.grid(row=0,column=0, sticky="nsew")

assessment_labal = Label(top_right_frame, text="Dates Assessment Before Cutting: " + str(random.randint(3000,5000)))
assessment_labal.grid(row=0, column=0, sticky="w", pady=50)

assessment_after_labal = Label(top_right_frame, text="Dates Assessment After Cutting: " + str(random.randint(1000,3000)))
assessment_after_labal.grid(row=1, column=0, sticky="w", pady=50)
assessment_after_labal.grid_forget()


##--------------------------Right Top 2 Frame-------------------------##
top2_right_frame = LabelFrame(frame_right,text="Cutting Option Section")
top2_right_frame.grid(row=1,column=0, sticky="nsew")



option_label = Label(top2_right_frame, text="Choose an option for operation:")
option_label.grid(row=1, column=0, sticky="w",pady=10)

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
        ge = Entry(top2_right_frame, width=28, borderwidth=2)
        ge.grid(row=4, column=0, sticky="w", padx=5, pady=10)

        b_submit = Button(top2_right_frame, text="Submit", command=submit_entry)
        b_submit.grid(row=4, column=0, sticky="e", padx=10, pady=10)

        b_clear = Button(top2_right_frame, text="Clear", command=clear_entry)
        b_clear.grid(row=4, column=1, sticky="w")
    else:
        ge = Entry(top2_right_frame, width=28, borderwidth=2, state=DISABLED)
        ge.grid(row=4, column=0, sticky="w", padx=5, pady=10)

        b_submit = Button(top2_right_frame, text="Submit", command=submit_entry, state=DISABLED)
        b_submit.grid(row=4, column=0, sticky="e", padx=10, pady=10)

        b_clear = Button(top2_right_frame, text="Clear", command=clear_entry, state=DISABLED)
        b_clear.grid(row=4, column=1, sticky="w")

    selectedRadio = Label(top2_right_frame, text="Option Selected: " + str(value))
    selectedRadio.grid(row=5, column=0, columnspan=2)

def clear_entry():
    ge.delete(0, END)

def submit_entry():
    global leading_Sansan
    global ge
    ge.delete(0, END)
    assessment_labal = Label(top_right_frame,
                             text="Dates Assessment Before Cutting: " + str(random.randint(3000, 5000)))
    assessment_labal.grid(row=0, column=0, sticky="w", pady=50)

    assessment_after_labal = Label(top_right_frame,
                                   text="Dates Assessment After Cutting: " + str(random.randint(-50, 50) + 1500))
    assessment_after_labal.grid(row=1, column=0, sticky="w", pady=50)
    assessment_labal.grid_forget()

    Sansan_Window = Toplevel()
    Sansan_Window.title('Puting The Leading Sansan By Yourself')

    screen_width_sansan = int(int(Sansan_Window.winfo_screenwidth()) * 0.92)
    screen_height_sansan = int(int(Sansan_Window.winfo_screenheight()) * 0.9)
    geometry = str(screen_width_sansan) + "x" + str(screen_height_sansan)
    Sansan_Window.geometry(geometry)
    palm_img1 = Image.open('images/palm.jpg')
    resized_image1 = palm_img1.resize((screen_width_sansan, screen_height_sansan), Image.ANTIALIAS)
    sansan_image = ImageTk.PhotoImage(resized_image1)

    # Grid Configurations
    Grid.rowconfigure(root, index=0, weight=2)
    Grid.columnconfigure(root, index=0, weight=2)


    my_Sansan_label = Label(Sansan_Window, image=sansan_image)
    my_Sansan_label.grid(row=0, column=0)
    quit_button = Button(Sansan_Window, text="I had finished drewing", command=Sansan_Window.destroy)
    quit_button.grid(row=1,column=0)
    #if leading_Sansan ==False:



Radiobutton(top2_right_frame, text="Manual marking on the image", variable=r, value="Manual marking", command=lambda : clicked(r.get())).grid(row=2, column=0, sticky="w")
Radiobutton(top2_right_frame, text="Enter input for the amount that will remain", variable=r, value="Input of amount", command=lambda : clicked(r.get())).grid(row=3, column=0, sticky="w")

# Input Box
ge = Entry(top2_right_frame, width=28, borderwidth=2, state=DISABLED)
ge.grid(row=4, column=0, sticky="w", padx=5, pady=10)

b_submit = Button(top2_right_frame, text="Submit", command=submit_entry, state=DISABLED)
b_submit.grid(row=4, column=0, sticky="e", padx=10, pady=10)

b_clear = Button(top2_right_frame, text="Clear", command=clear_entry, state=DISABLED)
b_clear.grid(row=4, column=1, sticky="w")

selectedRadio = Label(top2_right_frame, text="Option Selected: " + str(r.get()))
selectedRadio.grid(row=5, column=0, columnspan=2)

# Case we don't found the leading Sansan

##--------------------------Right Top 3 Frame-------------------------##
top3_right_frame = LabelFrame(frame_right,text="The lenth the robot move section")
top3_right_frame.grid(row=2,column=0, sticky="nsew", pady=20)

def range_calculator():
    return 40

L_length_range_labal = Label(top3_right_frame,text="The Distance The Robot Will Move Is: " +str(range_calculator()) + " Centimeter")
L_length_range_labal.grid(row=0, column=0, pady=10)
# L_length_range_labal.grid_forget()

##--------------------------Right Top 4 Frame-------------------------##

top4_right_frame = LabelFrame(frame_right, text="Confirm The process section")
top4_right_frame.grid(row=3,column=0, pady=20)

def confirmation_click():
    responed = messagebox.askyesno("Final Confirmation" , "Are you sure you want to do the cuttin? there is no way back from here!")
    Label(top4_right_frame, text=responed).pack()
    # if responed == 1:



final_confirmation = Button(top4_right_frame, text="Are you sure you want to cut?", command=confirmation_click)
final_confirmation.grid(row=0,column=0,pady=10,padx=65)
# final_confirmation.grid_forget()





#while TRUE:
#    root.update()
#    width = frame.winfo_width()
#    height = frame.winfo_height()
#    print("The width of the label is:", width,height, "pixels")

#b = Button(frame, text="Click Here")
#b.grid(row=1, column=0, sticky="nsew")


root.mainloop()
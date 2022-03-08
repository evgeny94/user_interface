import random
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('User Interface')
root.iconbitmap('images/icon.ico')

# For the submit button
num_clicked = 0

screen_width = int(int(root.winfo_screenwidth())*0.92)
screen_height = int(int(root.winfo_screenheight())*0.9)

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
frame_left = LabelFrame(root, text="Picture")
frame_left.grid(row=0, column=0, sticky="nsew")

# Frame Configuration
frame_left.rowconfigure(index=0, weight=1)
frame_left.columnconfigure(index=0, weight=1)

my_label = Label(frame_left, image=new_image)
my_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

##--------------------------Right Side-------------------------##
# Frame Creation
frame_right = LabelFrame(root, text="Information Section")
frame_right.grid(row=0, column=1, sticky="nsew")

# Frame Configuration
frame_right.rowconfigure(index=0, weight=1)
frame_right.rowconfigure(index=1, weight=1)
frame_right.rowconfigure(index=2, weight=1)
frame_right.rowconfigure(index=3, weight=0)

##--------------------------Right Top 1 Frame-------------------------##

top1_right_frame = LabelFrame(frame_right, text="Assessmention Section")
top1_right_frame.grid(row=0, column=0, sticky="nsew")

assessment_label = Label(top1_right_frame, text="Dates Assessment Before Cutting: " + str(random.randint(3000, 5000)))
assessment_label.grid(row=0, column=0, sticky="w", pady=10)

##--------------------------Right Top 2 Frame-------------------------##
top2_right_frame = LabelFrame(frame_right, text="Cutting Option Section")
top2_right_frame.grid(row=1, column=0, sticky="nsew")

option_label = Label(top2_right_frame, text="Choose an option for operation:")
option_label.grid(row=1, column=0, sticky="w", pady=10)

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

def range_calculator():
    return random.randint(50, 70)

def clear_entry():
    global L_length_range_label_unpressed
    global assessment_afterCut_label
    global L_length_range_label
    global num_clicked

    ge.delete(0, END)

    num_clicked = 0
    assessment_afterCut_label.grid_forget()
    L_length_range_label.grid_forget()
    L_length_range_label_unpressed = Label(top3_right_frame,
                                           text="The distance that the robot will pass will appear here\n after pressing on the submit button.",
                                           justify=LEFT)
    L_length_range_label_unpressed.grid(row=0, column=0, pady=10)

def submit_restart():
    global L_length_range_label_unpressed
    global assessment_afterCut_label
    global L_length_range_label

    assessment_afterCut_label.grid_forget()
    L_length_range_label.grid_forget()
    L_length_range_label_unpressed = Label(top3_right_frame,
                                           text="The distance that the robot will pass will appear here\n after pressing on the submit button.",
                                           justify=LEFT)
    L_length_range_label_unpressed.grid(row=0, column=0, pady=10)

def submit_entry():
    global ge
    global new_image
    global L_length_range_label
    global assessment_afterCut_label
    global L_length_range_label_unpressed
    global num_clicked

    num_clicked = num_clicked + 1

    # Number of clicks on submit for deleting previous grids
    # First time clicked
    if num_clicked == 1:
        found_respond = messagebox.askyesno("Manual decision about the <Leading Sansan>",
                                            "Has the computational system found the <Leading Sansan>?")
        # Leading Sansan found
        if found_respond == 1:
            assessment_afterCut_label = Label(top1_right_frame, text="Dates Assessment After Cutting: " + str(
                int(ge.get()) + random.randint(-50, 50)))
            assessment_afterCut_label.grid(row=1, column=0, sticky="w", pady=5)

            L_length_range_label_unpressed.grid_forget()
            L_length_range_label = Label(top3_right_frame, text="The distance that the robot will pass is: " + str(
                range_calculator()) + " Centimeters")
            L_length_range_label.grid(row=0, column=0, pady=10)
        # Leading Sansan not found
        else:
            Sansan_Window = Toplevel()
            Sansan_Window.title('Marking The Leading Sansan Manually')

            my_Sansan_label = Label(Sansan_Window, image=new_image)
            my_Sansan_label.grid(row=0, column=0)
            quit_button = Button(Sansan_Window, text="I had finished drawing", command=Sansan_Window.destroy)
            quit_button.grid(row=1, column=0, pady=5)
    # Already clicked
    else:
        submit_restart()
        found_respond = messagebox.askyesno("Manual decision about the <Leading Sansan>",
                                            "Has the computational system found the <Leading Sansan>?")
        # Leading Sansan found
        if found_respond == 1:
            assessment_afterCut_label = Label(top1_right_frame, text="Dates Assessment After Cutting: " + str(
                int(ge.get()) + random.randint(-50, 50)))
            assessment_afterCut_label.grid(row=1, column=0, sticky="w", pady=5)

            L_length_range_label_unpressed.grid_forget()
            L_length_range_label = Label(top3_right_frame, text="The distance that the robot will pass is: " + str(
                range_calculator()) + " Centimeters")
            L_length_range_label.grid(row=0, column=0, pady=10)
        # Leading Sansan not found
        else:
            Sansan_Window = Toplevel()
            Sansan_Window.title('Marking The Leading Sansan Manually')

            my_Sansan_label = Label(Sansan_Window, image=new_image)
            my_Sansan_label.grid(row=0, column=0)
            quit_button = Button(Sansan_Window, text="I had finished drawing", command=Sansan_Window.destroy)
            quit_button.grid(row=1, column=0, pady=5)





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

##--------------------------Right Top 3 Frame-------------------------##
top3_right_frame = LabelFrame(frame_right, text="Trajectory Length Section")
top3_right_frame.grid(row=2, column=0, sticky="nsew")

L_length_range_label_unpressed = Label(top3_right_frame,
                                       text="The distance that the robot will pass will appear here\n after pressing on the submit button.",
                                       justify=LEFT)
L_length_range_label_unpressed.grid(row=0, column=0, pady=10)


##--------------------------Right Top 4 Frame-------------------------##
top4_right_frame = LabelFrame(frame_right, text="Final Confirmation")
top4_right_frame.grid(row=3, column=0, sticky="nsew")

def confirmation_click():
    confirmation_respond = messagebox.askyesno("Final Confirmation", "Are you sure you want to do the cut? There is no way back from here.")

    # if confirmation_respond == 1:

final_confirmation = Button(top4_right_frame, text="Cut", command=confirmation_click, padx=10)
final_confirmation.pack(pady=10)

root.mainloop()
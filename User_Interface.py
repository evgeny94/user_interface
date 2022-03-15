import random
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('User Interface')
root.iconbitmap('images/icon.ico')

## --------------- Screen configurations --------------- ##
screen_width = int(int(root.winfo_screenwidth())*0.92)
screen_height = int(int(root.winfo_screenheight())*0.9)
print("root managed: " + str(screen_width) + ", " + str(screen_height))

screen_width1 = root.winfo_screenwidth()
screen_height1 = root.winfo_screenheight()
print("root: " + str(screen_width1) + ", " + str(screen_height1))

geometry = str(screen_width) + "x" + str(screen_height)

root.geometry(geometry)

## --------------- Frames --------------- ##
# Frame Creation Left
frame_left = LabelFrame(root, text="Picture")
frame_left.grid(row=0, column=0, sticky="nsew")

# Frame Configuration Left
frame_left.rowconfigure(index=0, weight=2)
frame_left.columnconfigure(index=0, weight=2)

# Frame Creation Right
frame_right = LabelFrame(root, text="Information Section")
frame_right.grid(row=0, column=1, sticky="nsew")

# Frame Configuration Right
frame_right.rowconfigure(index=0, weight=1)
frame_right.rowconfigure(index=1, weight=1)
frame_right.rowconfigure(index=2, weight=1)
frame_right.rowconfigure(index=3, weight=0)

# Right Top 1 Frame
top1_right_frame = LabelFrame(frame_right, text="Assessmention Section")
top1_right_frame.grid(row=0, column=0, sticky="nsew")

# Right Top 2 Frame
top2_right_frame = LabelFrame(frame_right, text="Cutting Option Section")
top2_right_frame.grid(row=1, column=0, sticky="nsew")

# Right Top 3 Frame
top3_right_frame = LabelFrame(frame_right, text="Trajectory Length Section")
top3_right_frame.grid(row=2, column=0, sticky="nsew")

# Right Top 4 Frame
top4_right_frame = LabelFrame(frame_right, text="Final Confirmation")
top4_right_frame.grid(row=3, column=0, sticky="nsew")

## --------------- Variables & Image --------------- ##
# For the submit button
num_clicked = 0

# Image + Configurations
palm_img = Image.open('images/palm.jpg')

resized_image = palm_img.resize((screen_width, screen_height), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas_san = Canvas()

## --------------- Functions --------------- ##
# --------------- Main Image Drawing ---------------
def get_xy(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw(event):
    global lasx, lasy, line
    line = canvas.create_line((lasx, lasy, event.x, event.y), width=3, tags='currentline')
    lasx, lasy = event.x, event.y

def clear_drawing():
    global canvas, line

    canvas.delete('currentline')
    L_length_range_label['text'] = "The distance that the robot will pass will appear here\n after pressing on the submit button."
    assessment_afterCut_label['text'] = ""
    final_confirmation['state'] = DISABLED

def doneStroke(event):
    canvas.itemconfigure('currentline', width=3)

def end_sansan_window(type):
    Sansan_Window.destroy()
    if type == "numeric input":
        assessment_afterCut_label['text'] = "Dates Assessment After Cutting: " + str(
            int(ge.get()) + random.randint(-50, 50))
    else:
        assessment_afterCut_label['text'] = "Dates Assessment After Cutting: " + str(
            int(random.randint(3000, 5000) / 2.5 + random.randint(-50, 50)))

    L_length_range_label['text'] = "The distance that the robot will pass is: " + str(
        range_calculator()) + " Centimeters"

    # Enabling Cut Button
    final_confirmation['state'] = NORMAL
# --------------- Sansan Drawing ---------------
def draw_san(event):
    global lasx, lasy, line_san
    line_san = canvas_san.create_line((lasx, lasy, event.x, event.y), width=5, tags='line_san')
    lasx, lasy = event.x, event.y

def clear_drawing_san():
    global canvas_san, line_san
    canvas_san.delete('line_san')

def done_san(event):
    canvas_san.itemconfigure('line_san', width=5)

# --------------- ## --------------- #
# In case the Leading Sansan not found
def leading_san_not_found(type):
    global canvas_san, final_confirmation, Sansan_Window
    # Disabling Cut Button
    final_confirmation['state'] = DISABLED

    # Open new window for drawing the sansan
    Sansan_Window = Toplevel()
    Sansan_Window.title('Marking The Leading Sansan Manually')

    # Top Frame
    top_frame = LabelFrame(Sansan_Window, text="TOP")
    top_frame.grid(row=0, column=0, sticky="nsew")

    # Bottom Frame
    bottom_frame = LabelFrame(Sansan_Window, text="BOTTOM")
    bottom_frame.grid(row=1, column=0, sticky="nsew")

    # Grid configuration
    Grid.rowconfigure(Sansan_Window, index=0, weight=2)
    Grid.columnconfigure(Sansan_Window, index=0, weight=2)

    # Canvas
    canvas_san = Canvas(top_frame)
    canvas_san.pack(anchor='nw', fill='both', expand=1)
    canvas_san.create_image(0, 0, image=new_image, anchor='nw')

    # Enable Drawing
    canvas_san.bind("<Button-1>", get_xy)
    canvas_san.bind("<B1-Motion>", draw_san)
    canvas_san.bind("<B1-ButtonRelease>", done_san)

    # Exit button
    quit_button = Button(bottom_frame, text="Save and Continue", command=lambda : end_sansan_window(type))
    quit_button.grid(row=0, column=0, padx=10, pady=5)

    # Clear button
    clear_button = Button(bottom_frame, text="Clear", command=clear_drawing_san)
    clear_button.grid(row=0, column=1, padx=10, pady=5)

def myDelete():
    selectedRadio.grid_forget()

def clicked(value):
    global selectedRadio, ge, b_submit, b_clear, b_clear_draw, final_confirmation, assessment_afterCut_label

    myDelete()
    L_length_range_label['text'] = "The distance that the robot will pass will appear here\n after pressing on the submit button."
    final_confirmation['state'] = DISABLED
    if value == "Input of amount":
        # Clear and Disable Drawing
        clear_drawing()
        canvas.bind("<Button-1>", 'none')
        canvas.bind("<B1-Motion>", 'none')
        canvas.bind("<B1-ButtonRelease>", 'none')

        # Entry
        ge['state'] = NORMAL

        # Submit Button
        b_submit['state'] = NORMAL

        # Clear Entry Button
        b_clear['state'] = NORMAL

        # Completed Drawing Button DISABLED
        b_done_draw['state'] = DISABLED

        # Clear Drawing Button DISABLED
        b_clear_draw['state'] = DISABLED
    else:
        # Forget previous assessment
        assessment_afterCut_label['text'] = ""

        # Enable Drawing
        canvas.bind("<Button-1>", get_xy)
        canvas.bind("<B1-Motion>", draw)
        canvas.bind("<B1-ButtonRelease>", doneStroke)

        # Entry DISABLED
        ge['state'] = DISABLED

        # Submit Button DISABLED
        b_submit['state'] = DISABLED

        # Clear Entry Button DISABLED
        b_clear['state'] = DISABLED

        # Completed Drawing Button DISABLED
        b_done_draw['state'] = NORMAL

        # Clear Drawing Button DISABLED
        b_clear_draw['state'] = NORMAL

    # Selected String From Radio Buttons
    selectedRadio['text'] = "Option Selected: " + str(value)
    selectedRadio.grid(row=6, column=0, columnspan=2)

def range_calculator():
    return random.randint(50, 70)

def clear_entry():
    global assessment_afterCut_label, L_length_range_label, num_clicked, final_confirmation

    ge.delete(0, END)

    num_clicked = 0
    assessment_afterCut_label['text'] = ""
    L_length_range_label['state'] = NORMAL
    L_length_range_label['text'] = "The distance that the robot will pass will appear here\n after pressing on the submit button."

    # Disabling Cut Button
    final_confirmation['state'] = DISABLED

def submit_restart():
    global assessment_afterCut_label, L_length_range_label, final_confirmation

    assessment_afterCut_label['text'] = ""
    L_length_range_label['state'] = NORMAL

    # Disabling Cut Button
    final_confirmation['state'] = DISABLED

def submit_entry():
    global ge, new_image, L_length_range_label, assessment_afterCut_label, num_clicked, final_confirmation

    num_clicked = num_clicked + 1

    # Number of clicks on submit for deleting previous grids
    # First time clicked
    if num_clicked == 1:
        found_respond = messagebox.askyesno("Manual decision about the <Leading Sansan>",
                                            "Has the computational system found the <Leading Sansan>?")
        # Leading Sansan found
        if found_respond == 1:
            assessment_afterCut_label['text'] = "Dates Assessment After Cutting: " + str(
                int(ge.get()) + random.randint(-50, 50))

            L_length_range_label['text'] = "The distance that the robot will pass is: " + str(
                range_calculator()) + " Centimeters"

            # Enabling Cut Button
            final_confirmation['state'] = NORMAL

        # Leading Sansan not found
        else:
            leading_san_not_found("numeric input")
    # Already clicked
    else:
        submit_restart()
        found_respond = messagebox.askyesno("Manual decision about the <Leading Sansan>",
                                            "Has the computational system found the <Leading Sansan>?")
        # Leading Sansan found
        if found_respond == 1:
            assessment_afterCut_label['text'] = "Dates Assessment After Cutting: " + str(
                int(ge.get()) + random.randint(-50, 50))

            L_length_range_label['text'] = "The distance that the robot will pass is: " + str(
                range_calculator()) + " Centimeters"

            # Enabling Cut Button
            final_confirmation['state'] = NORMAL

        # Leading Sansan not found
        else:
            leading_san_not_found("numeric input")

def confirmation_click():
    confirmation_respond = messagebox.askyesno("Final Confirmation", "Are you sure you want to do the cut? There is no way back from here.")

    # if confirmation_respond == 1:

def done_drawing():
    found_respond = messagebox.askyesno("Manual decision about the <Leading Sansan>",
                                        "Has the computational system found the <Leading Sansan>?")
    # Leading Sansan found
    if found_respond == 1:
        assessment_afterCut_label['text'] = "Dates Assessment After Cutting: " + str(int(random.randint(3000, 5000)/2.5 + random.randint(-50, 50)))

        L_length_range_label['text'] = "The distance that the robot will pass is: " + str(
            range_calculator()) + " Centimeters"

        # Enabling Cut Button
        final_confirmation['state'] = NORMAL

    # Leading Sansan not found
    else:
        leading_san_not_found("marking")

##------------##-------------- MAIN -------------##------------##
# Grid Configurations
Grid.rowconfigure(root, index=0, weight=2)
Grid.columnconfigure(root, index=0, weight=2)
#Grid.rowconfigure(root, index=1, weight=1)


##--------------------------Left Side-------------------------##
# Main Canvas
canvas = Canvas(frame_left)
canvas.pack(anchor='nw', fill='both', expand=1)
canvas.create_image(0, 0, image=new_image, anchor='nw')

##--------------------------Right Side-------------------------##
##--------------------------Right Top 1 Frame-------------------------##

assessment_label = Label(top1_right_frame, text="Dates Assessment Before Cutting: " + str(random.randint(3000, 5000)))
assessment_label.grid(row=0, column=0, sticky="w", pady=10)

assessment_afterCut_label = Label(top1_right_frame, text="")
assessment_afterCut_label.grid(row=1, column=0, sticky="w", pady=5)

##--------------------------Right Top 2 Frame-------------------------##

option_label = Label(top2_right_frame, text="Choose an option for operation:")
option_label.grid(row=1, column=0, sticky="w", pady=10)

# Radio Buttons
r = StringVar()
r.set("None")

Radiobutton(top2_right_frame, text="Manual marking on the image", variable=r, value="Manual marking", command=lambda : clicked(r.get())).grid(row=2, column=0, sticky="w")
Radiobutton(top2_right_frame, text="Enter input for the amount that will remain", variable=r, value="Input of amount", command=lambda : clicked(r.get())).grid(row=4, column=0, sticky="w")

# Completed Drawing Button DISABLED
b_done_draw = Button(top2_right_frame, text="Continue", command=done_drawing, state=DISABLED)
b_done_draw.grid(row=3, column=0, padx=50, pady=10, sticky="w")

# Clear Drawing Button DISABLED
b_clear_draw = Button(top2_right_frame, text="Clear Drawing", command=clear_drawing, state=DISABLED)
b_clear_draw.grid(row=3, column=0, padx=50, pady=10, sticky="e", columnspan=2)

# Input Box DISABLED
ge = Entry(top2_right_frame, width=28, borderwidth=2, state=DISABLED)
ge.grid(row=5, column=0, sticky="w", padx=5, pady=10)

# Submit Button DISABLED
b_submit = Button(top2_right_frame, text="Submit", command=submit_entry, state=DISABLED)
b_submit.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# Clear Entry Button DISABLED
b_clear = Button(top2_right_frame, text="Clear", command=clear_entry, state=DISABLED)
b_clear.grid(row=5, column=1, sticky="w")

# Selected String From Radio Buttons
selectedRadio = Label(top2_right_frame, text="Option Selected: " + str(r.get()))
selectedRadio.grid(row=6, column=0, columnspan=2)

##--------------------------Right Top 3 Frame-------------------------##

L_length_range_label = Label(top3_right_frame,
                                       text="The distance that the robot will pass will appear here\n after pressing on the submit button.",
                                       justify=LEFT)
L_length_range_label.grid(row=0, column=0, pady=10)

##--------------------------Right Top 4 Frame-------------------------##

final_confirmation = Button(top4_right_frame, text="Cut", command=confirmation_click, padx=10, state=DISABLED)
final_confirmation.pack(pady=10)

root.mainloop()
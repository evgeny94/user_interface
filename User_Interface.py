import random, math
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
frame_left = LabelFrame(root, text="Picture", labelanchor='n', bg='white', font='sans 10 bold')
frame_left.grid(row=0, column=0, sticky="nsew")

# Frame Creation Right
frame_right = LabelFrame(root, text="Information", labelanchor='n', bg='white', font='sans 11 bold')
frame_right.grid(row=0, column=1, sticky="nsew")

# Frame Configuration Right
frame_right.rowconfigure(index=0, weight=0)
frame_right.rowconfigure(index=1, weight=1)
frame_right.rowconfigure(index=2, weight=1)
frame_right.rowconfigure(index=3, weight=0)

# Right Top 1 Frame
top1_right_frame = LabelFrame(frame_right, text="Assessmention", labelanchor='n', bg='white')
# top1_right_frame.grid(row=0, column=0, sticky="nsew")

# Right Top 2 Frame
top2_right_frame = LabelFrame(frame_right, text="Operations", labelanchor='n', bg='white')
# top2_right_frame.grid(row=1, column=0, sticky="nsew")

# Right Top 3 Frame
top3_right_frame = LabelFrame(frame_right, labelanchor='n', bg='white')
# top3_right_frame.grid(row=2, column=0, sticky="nsew")

# Right Top 4 Frame
top4_right_frame = LabelFrame(frame_right, labelanchor='n', bg='white')
# top4_right_frame.grid(row=3, column=0, sticky="nsew")

## --------------- Variables & Image --------------- ##
# For the submit button
num_clicked = 0

# Image + Configurations
palm_img = Image.open('images/palm.jpg')
palm_img_san = Image.open('images/palm.jpg')
width_pre, heigth_pre, cnt = 0, 0, 0
width_pre_san, heigth_pre_san, cnt_san = 0, 0, 0
resized_image = palm_img.resize((screen_width, screen_height), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas_san = Canvas()
o1, o2 = 580, 675
R = 450
global new_image_san

# curve points
global points_san
global temp_arc_san
global released_san
released_san = False
points_san = []
temp_arc_san = None
found = False

#for finding sansun
global finding_chance

#final confirmation
global final_confirmation
## --------------- Functions --------------- ##

#-----------------show/hide functions-----------------------

def Hide_2_last_frames():
    top3_right_frame['text'] = ""
    # L_length_range_label_text.place_forget()
    # L_length_range_label.place_forget()
    L_length_range_label_text.grid_forget()
    L_length_range_label.grid_forget()
    assessment_afterCut_label['text'] = ""
    top4_right_frame['text'] = ""
    final_confirmation.pack_forget()

def Show_2_last_frames():
    top3_right_frame['text'] = "Results Section"
    L_length_range_label_text.grid(row=3, column=0, pady=5, sticky="e")
    L_length_range_label.grid(row=4, column=0, pady=5)
    top4_right_frame['text'] = "Final Confirmation"
    final_confirmation.pack(pady=10)
    final_confirmation_helper.pack_forget()

# --------------- Main Image Drawing ---------------
def get_xy(event):
    global firstx, firsty, line
    firstx, firsty = event.x, event.y
    line = canvas.create_line(firstx, firsty, firstx, firsty, fill="#00FFFF", width=8, tags='currentline')

def draw(event):
    canvas.coords('currentline', firstx, firsty, event.x, event.y)

def clear_drawing():
    global canvas
    canvas.delete('currentline')
    Hide_2_last_frames()
    assessment_afterCut_label['text'] = ""
    assessment_afterCut_num_label['text'] = ""
    assessment_afterCut_num_label['relief'] = FLAT
    assessment_afterCut_num_label['bg'] = 'white'
    final_confirmation['state'] = DISABLED

def doneStroke(event):
    global line
    line = canvas.itemconfigure('currentline', width=8)
    print('Canvas coords:' + str(canvas.coords('currentline')))

def create_random_line():
    global line
    x1, y1, x2, y2 = random.randint(70, 105), random.randint(92, 148),\
                     random.randint(373, 425), random.randint(565, 665)
    line = canvas.create_line(x1, y1, x2, y2, width=8, tags='randomcurrentline')

def end_spikelet_window():
    global myArc
    width, height = new_image.width(), new_image.height()
    width_pre_4_san, height_pre_4_san = new_image_san.width(), new_image_san.height()
    x_arc_san = [point_san[0] for point_san in points_san]
    y_arc_san = [point_san[1] for point_san in points_san]
    x_arc_san_0, y_arc_san_0 = x_arc_san[0], y_arc_san[0]
    x_arc_san_0, y_arc_san_0 = float(round((x_arc_san_0 / width_pre_4_san) * width)), \
                               float(round((y_arc_san_0 / height_pre_4_san) * height))
    x_arc_san_last, y_arc_san_last = x_arc_san[-1], y_arc_san[-1]
    x_arc_san_last, y_arc_san_last = float(round((x_arc_san_last / width_pre_4_san) * width)), \
                                     float(round((y_arc_san_last / height_pre_4_san) * height))
    canvas.delete('manualArcSan')
    myArc = canvas.create_arc(x_arc_san_0, y_arc_san_0, x_arc_san_last, y_arc_san_last, start=63,
                              extent=92,
                              style=ARC,
                              outline="#4B0082",
                              width=8,
                              tags='manualArcSan')
    Spikelet_Window.destroy()

# --------------- Spiklet Drawing ---------------
def get_xy_san(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_san(event):
    global lasx, lasy, line_san
    line_san = canvas_san.create_line((lasx, lasy, event.x, event.y), width=8, tags='line_san')
    lasx, lasy = event.x, event.y

def clear_drawing_san():
    global canvas_san, line_san
    canvas_san.delete('line_san')
    canvas_san.delete('manualArcSan')

def done_san(event):
    canvas_san.itemconfigure('line_san', width=8)

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle_arc = _create_circle_arc

#########################################################################################
def move_san(event):
    global canvas_san, lasx, lasy
    canvas_san.move('manualArcSan', event.x-lasx, event.y-lasy)
    lasx, lasy = event.x, event.y

def arc_san():
    global myArc, canvas_san
    x_arc_san = [point_san[0] for point_san in points_san]
    y_arc_san = [point_san[1] for point_san in points_san]
    myArc = canvas_san.create_arc(x_arc_san[0], y_arc_san[0], x_arc_san[-1], y_arc_san[-1], start=63,
                                extent=92,
                                style=ARC,
                                outline="#4B0082",
                                width=8,
                                tags='manualArcSan')
    return myArc

def motion_san(event):
    global temp_arc_san, points_san, released_san
    if released_san == True:
        points_san = []
        canvas_san.delete('manualArcSan')
        released_san = False
    points_san.append([event.x, event.y])
    if temp_arc_san != None:
        canvas_san.delete(temp_arc_san)
    temp_arc_san = arc_san()


def on_click_release_san(event):
    global released_san
    arc_san()
    released_san = True
#########################################################################################

# --------------- ## --------------- #
def size_changed_san(event):
    global width_pre_san, heigth_pre_san, cnt_san
    width_san, heigth_san = canvas_san.winfo_width(), canvas_san.winfo_height()
    cnt_san = cnt_san + 1
    if cnt_san > 1 and (width_pre_san != width_san or heigth_pre_san != heigth_san):
        width_pre_san, heigth_pre_san = canvas_san.winfo_width(), canvas_san.winfo_height()
        size_san(event)
    else:
        pass

def size_san(event):
    global new_image_san, resized_image_san, canvas_san

    width_san, heigth_san = canvas_san.winfo_width(), canvas_san.winfo_height()
    print('Canvas size:', width_san, 'x', heigth_san)

    resized_image_san = palm_img_san.resize((width_san, heigth_san), Image.ANTIALIAS)
    new_image_san = ImageTk.PhotoImage(resized_image_san)
    canvas_san.itemconfig(img_on_canvas_san, image=new_image_san)

# In case the Leading Spikelet not found
def manual_spikelet_drawing():
    global canvas_san, final_confirmation, Spikelet_Window, img_on_canvas_san
    # Disabling Cut Button
    final_confirmation['state'] = DISABLED

    # Open new window for drawing the spikelet
    Spikelet_Window = Toplevel()
    Spikelet_Window.title('Marking The Leading Spikelet Manually')

    # Top Frame
    blank_space = "_"
    top_frame = LabelFrame(Spikelet_Window, text="Picture", labelanchor='n', bg="white")
    top_frame.grid(row=0, column=0, sticky="nsew")

    # Bottom Frame
    bottom_frame = LabelFrame(Spikelet_Window, text="Buttons", labelanchor='n', bg="white")
    bottom_frame.grid(row=1, column=0, sticky="nsew")

    # Grid configuration
    Grid.rowconfigure(Spikelet_Window, index=0, weight=2)
    Grid.columnconfigure(Spikelet_Window, index=0, weight=2)

    # Frame configuration
    top_frame.rowconfigure(index=0, weight=2)
    top_frame.columnconfigure(index=0, weight=2)
    bottom_frame.rowconfigure(index=0, weight=1)
    bottom_frame.columnconfigure(index=0, weight=1)
    bottom_frame.columnconfigure(index=1, weight=1)

    # Canvas
    canvas_san = Canvas(top_frame, bg="white")
    canvas_san.pack(anchor='nw', fill='both', expand=1)
    img_on_canvas_san = canvas_san.create_image(0, 0, image=new_image, anchor='nw')

    # Enable Drawing
    # canvas_san.bind("<Button-1>", get_xy_san)
    # canvas_san.bind("<B1-Motion>", draw_san)
    # canvas_san.bind("<B1-ButtonRelease>", done_san)
    #
    canvas_san.bind("<B1-Motion>", motion_san)
    canvas_san.bind("<ButtonRelease-1>", on_click_release_san)
    Spikelet_Window.bind("<Button-3>", get_xy_san)
    Spikelet_Window.bind("<B3-Motion>", move_san)
    # Exit button
    quit_button = Button(bottom_frame, text="Save and Continue", command=end_spikelet_window)
    quit_button.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    # Clear button
    clear_button = Button(bottom_frame, text="Clear", command=clear_drawing_san)
    clear_button.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    # Hook window size changes
    Spikelet_Window.bind('<Configure>', size_changed_san)

def myDelete():
    selectedRadio.grid_forget()
    selectedRadioValue.grid_forget()

def clicked(value):
    global selectedRadio, selectedRadioValue, ge, b_submit, b_clear, b_clear_draw, final_confirmation, assessment_afterCut_label, assessment_afterCut_num_label, r_value

    r_value = value
    myDelete()
    final_confirmation['state'] = DISABLED
    if value == "Input of amount":
        # Clear and Disable Drawing
        clear_drawing()
        canvas.bind("<Button-1>", 'none')
        canvas.bind("<B1-Motion>", 'none')
        canvas.bind("<B1-ButtonRelease>", 'none')

        # Hide 2 last frames
        Hide_2_last_frames()

        # Entry
        ge['state'] = NORMAL

        # Submit Button
        # b_submit['state'] = NORMAL

        # Clear Entry Button
        # b_clear['state'] = NORMAL

        # Completed Drawing Button DISABLED
        # b_done_draw['state'] = DISABLED

        # Clear Drawing Button DISABLED
        # b_clear_draw['state'] = DISABLED
    else:
        # Forget previous assessment and drawings
        assessment_afterCut_label['text'] = ""
        assessment_afterCut_num_label['text'] = ""
        assessment_afterCut_num_label['relief'] = FLAT
        assessment_afterCut_num_label['bg'] = 'white'
        canvas.delete('randomcurrentline')

        # Enable Drawing
        canvas.bind("<Button-1>", get_xy)
        canvas.bind("<B1-Motion>", draw)
        canvas.bind("<B1-ButtonRelease>", doneStroke)

        #Hide 2 last frames
        Hide_2_last_frames()

        # Entry DISABLED & Clear
        ge.delete(0,END)
        ge['state'] = DISABLED

        # Submit Button DISABLED
        # b_submit['state'] = DISABLED

        # Clear Entry Button DISABLED
        # b_clear['state'] = DISABLED

        # Completed Drawing Button DISABLED
        # b_done_draw['state'] = NORMAL

        # Clear Drawing Button DISABLED
        # b_clear_draw['state'] = NORMAL

    # Selected String From Radio Buttons
    selectedRadio['text'] = "Option Selected: "
    selectedRadio.grid(row=7, column=0, columnspan=2)
    selectedRadioValue['text'] = str(value)
    selectedRadioValue.grid(row=8, column=0, columnspan=2)


def range_calculator():
    return random.randint(50, 70)

def clear_entry():
    global assessment_afterCut_label, assessment_afterCut_num_label, L_length_range_label_text, L_length_range_label, num_clicked, final_confirmation

    ge.delete(0, END)
    canvas.delete('randomcurrentline')
    num_clicked = 0
    Hide_2_last_frames()
    assessment_afterCut_label['text'] = ""
    assessment_afterCut_num_label['text'] = ""
    assessment_afterCut_num_label['relief'] = FLAT
    assessment_afterCut_num_label['bg'] = 'white'

    # Disabling Cut Button
    final_confirmation['state'] = DISABLED

def submit_restart():
    global assessment_afterCut_label, assessment_afterCut_num_label, L_length_range_label_text, L_length_range_label, final_confirmation

    assessment_afterCut_label['text'] = ""
    assessment_afterCut_num_label['text'] = ""
    assessment_afterCut_num_label['relief'] = FLAT
    assessment_afterCut_num_label['bg'] = 'white'
    L_length_range_label_text['state'] = NORMAL
    L_length_range_label['state'] = NORMAL
    canvas.delete('randomcurrentline')
    # Disabling Cut Button
    final_confirmation['state'] = DISABLED

def submit_entry():
    global ge, new_image, L_length_range_label_text, assessment_afterCut_label, assessment_afterCut_num_label, num_clicked, final_confirmation

    valid = ge.get().isdigit()
    # Number of clicks on submit for deleting previous grids
    # First time clicked
    if valid == True:
        if int(ge.get()) < assessment_before:
            if num_clicked == 1:
                Show_2_last_frames()
                assessment_afterCut_label['text'] = "Dates Assessment After Cutting: "
                assessment_afterCut_num_label['text'] = str(int(ge.get()) + random.randint(-50, 50))
                assessment_afterCut_num_label['relief'] = GROOVE
                assessment_afterCut_num_label['bg'] = None
                L_length_range_label_text['text'] = "The distance that the robot will pass is:"
                L_length_range_label['text'] = str(range_calculator()) + " Centimeters"

                # Enabling Cut Button
                final_confirmation['state'] = NORMAL

                # Random Line
                create_random_line()
            # Already clicked
            else:
                submit_restart()
                Show_2_last_frames()
                assessment_afterCut_label['text'] = "Dates Assessment After Cutting: "
                assessment_afterCut_num_label['text'] = str(int(ge.get()) + random.randint(-50, 50))
                assessment_afterCut_num_label['relief'] = GROOVE
                assessment_afterCut_num_label['bg'] = None
                L_length_range_label_text['text'] = "The distance that the robot will pass is:"
                L_length_range_label['text'] = str(range_calculator()) + " Centimeters"
                # Enabling Cut Button
                final_confirmation['state'] = NORMAL
                # Random Line
                create_random_line()
        else:
            clear_entry()
            messagebox.showerror("Entry Box Error", "The number is equal or greater than the initial assessment!\nPlease try again.")
    else:
        clear_entry()
        messagebox.showerror("Entry Box Error", "This Entry Box may contain only digits and positive numbers!\nPlease try again.")

def confirmation_click():
    confirmation_respond = messagebox.askyesno("Final Confirmation", "Are you sure you want to do the cut? There is no way back from here.")

    # if confirmation_respond == 1:

def done_drawing():
    Show_2_last_frames()
    assessment_afterCut_label['text'] = "Dates Assessment After Cutting: "
    assessment_afterCut_num_label['text'] = str(int(random.randint(3000, 5000)/2.5 + random.randint(-50, 50)))
    assessment_afterCut_num_label['relief'] = GROOVE
    assessment_afterCut_num_label['bg'] = None
    L_length_range_label_text['text'] = "The distance that the robot will pass is:"
    L_length_range_label['text'] = str(range_calculator()) + " Centimeters"
    # Enabling Cut Button
    final_confirmation['state'] = NORMAL

def found_leading_sansun():
    # Found
    if random.uniform(0, 1) <= 0.5:
        return True
    # Not Found
    else:
        return False

def redraw_line():
    global canvas
    width, heigth = canvas.winfo_width(), canvas.winfo_height()
    if len(canvas.coords("currentline")) != 0:
        x1, y1, x2, y2 = canvas.coords("currentline")[0], canvas.coords("currentline")[1],\
                         canvas.coords("currentline")[2], canvas.coords("currentline")[3]

        x1_new, y1_new, x2_new, y2_new = float(round((x1/width_pre_4_line)*width)), float(round((y1/height_pre_4_line)*heigth)),\
                                         float(round((x2/width_pre_4_line)*width)), float(round((y2/height_pre_4_line)*heigth))

        canvas.coords('currentline', x1_new, y1_new, x2_new, y2_new)
        print("currentline:" + str(canvas.coords('currentline')))

    elif len(canvas.coords("randomcurrentline")) != 0:
        x1, y1, x2, y2 = canvas.coords("randomcurrentline")[0], canvas.coords("randomcurrentline")[1],\
                         canvas.coords("randomcurrentline")[2], canvas.coords("randomcurrentline")[3]

        x1_new, y1_new, x2_new, y2_new = float(round((x1/width_pre_4_line)*width)), float(round((y1/height_pre_4_line)*heigth)),\
                                         float(round((x2/width_pre_4_line)*width)), float(round((y2/height_pre_4_line)*heigth))

        canvas.coords('randomcurrentline', x1_new, y1_new, x2_new, y2_new)
    else:
        pass

def redraw_arc():
    global canvas, R, o1, o2, found
    print(found)
    width, heigth = canvas.winfo_width(), canvas.winfo_height()
    if found == True:
        print("width, heigth:" + str(width), str(heigth))
        if width_pre_4_line > 1 and height_pre_4_line > 1:
            x1_arc, y1_arc = o1, o2 + R
            print("x1_arc, y1_arc:" + str(o1), str(o2 + R))
            o1, o2 = float(round((o1 / width_pre_4_line) * width)), \
                     float(round((o2 / height_pre_4_line) * heigth))
            print("o1_new, o2_new:" + str(o1), str(o2))
            x1_arc_new, y1_arc_new = float(round((x1_arc / width_pre_4_line) * width)), \
                                     float(round((y1_arc / height_pre_4_line) * heigth))
            print("x1_arc_new, y1_arc_new:" + str(x1_arc_new), str(y1_arc_new))
            R = float(round(math.sqrt((x1_arc_new - o1) ** 2 + (y1_arc_new - o2) ** 2)))
            canvas.delete('currentArc')
            print("R:" + str(R))
            camvas_arc = canvas.create_circle_arc(o1, o2, R, style="arc", outline="#4B0082", width=8,
                                                  start=90 - 27, end=90 + 65, tags='currentArc') #what happend here?
        else:
            pass
    else:
        if len(points_san) > 0:
            x_arc_san = [point_san[0] for point_san in points_san]
            y_arc_san = [point_san[1] for point_san in points_san]
            x_arc_san_0, y_arc_san_0 = x_arc_san[0], y_arc_san[0]
            x_arc_san_0, y_arc_san_0 = float(round((x_arc_san_0 / width_pre_4_line) * width)), \
                                       float(round((y_arc_san_0 / height_pre_4_line) * heigth))
            x_arc_san_last, y_arc_san_last = x_arc_san[-1], y_arc_san[-1]
            x_arc_san_last, y_arc_san_last = float(round((x_arc_san_last / width_pre_4_line) * width)), \
                                             float(round((y_arc_san_last / height_pre_4_line) * heigth))
            canvas.delete('manualArcSan')
            myArc = canvas.create_arc(x_arc_san_0, y_arc_san_0, x_arc_san_last, y_arc_san_last, start=63,
                                      extent=92,
                                      style=ARC,
                                      outline="#4B0082",
                                      width=8,
                                      tags='manualArcSan')
        else:
            pass

def size_changed(event):
    global width_pre, heigth_pre, cnt, width_pre_4_line, height_pre_4_line
    width, heigth = canvas.winfo_width(), canvas.winfo_height()
    cnt = cnt + 1
    if cnt > 1 and (width_pre != width or heigth_pre != heigth):
        width_pre_4_line, height_pre_4_line = width_pre, heigth_pre
        width_pre, heigth_pre = canvas.winfo_width(), canvas.winfo_height()
        size(event)
    else:
        pass

def size(event):
    global new_image, resized_image, canvas

    width, heigth = canvas.winfo_width(), canvas.winfo_height()
    print('Canvas size:', width, 'x', heigth)

    resized_image = palm_img.resize((width, heigth), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(img_on_canvas, image=new_image)
    redraw_line()
    redraw_arc()

def start_spikelet_configuration():
    global found
    found = found_leading_sansun()
    if found == True:
        camvas_arc = canvas.create_circle_arc(o1, o2, R, style="arc", outline="#4B0082", width=8,
                                              start=90 - 27, end=90 + 65, tags='currentArc')
        messagebox.showinfo("Information regards the <Leading Spikelet>",
                            "The computational system found an optional <Leading Spikelet>")
        # Asking if it is a good leading spikelet
        found_satisfying = messagebox.askyesno("Manual decision about the <Leading Spikelet>",
                                            "Has the computational system found a satisfying <Leading Spikelet>?")
        if found_satisfying == 1:
            pass
        else:
            found = False
            canvas.delete('currentArc')
            manual_spikelet_drawing()

    else:
        messagebox.showinfo("Information regards the <Leading Spikelet>",
                            "The computational system not succeeded \n"
                            "to find a <Leading Spikelet>\n\nPlease draw one manually.")
        manual_spikelet_drawing()

    # Redraw Leading Spikelet
    b_redraw = Button(top1_right_frame, text="Redraw Leading Spikelet", command=redraw_leading_spikelet, anchor=CENTER)
    b_redraw.grid(row=2, column=0, pady=10 ) #, sticky="w"

def start_user_interface():
    b_start_interface.pack_forget()
    start_label.pack_forget()
    # Right Top 1 Frame
    top1_right_frame.grid(row=0, column=0, sticky="nsew")

    # Right Top 2 Frame
    top2_right_frame.grid(row=1, column=0, sticky="nsew")

    # Right Top 3 Frame
    top3_right_frame.grid(row=2, column=0, sticky="nsew")

    # Right Top 4 Frame
    top4_right_frame.grid(row=3, column=0, sticky="nsew")

    start_spikelet_configuration()



def redraw_leading_spikelet():
    canvas.delete('currentArc')
    canvas.delete('manualArcSan')
    clear_drawing()
    clear_entry()
    manual_spikelet_drawing()



def univarsal_continue():
    global r_value
    if r_value == "Input of amount":
        submit_entry()
    else:
        done_drawing()


def univarsal_clear():
    global r_value
    if r_value == "Input of amount":
        clear_entry()
    else:
        clear_drawing()


##------------##-------------- MAIN -------------##------------##
# Hook window size changes
root.bind('<Configure>', size_changed)
# Grid Configurations
Grid.rowconfigure(root, index=0, weight=2)
Grid.columnconfigure(root, index=0, weight=2)
Grid.columnconfigure(top2_right_frame, index=0, weight=1)
#Grid.rowconfigure(root, index=1, weight=1)


##--------------------------Left Side-------------------------##
# Main Canvas
canvas = Canvas(frame_left)
canvas.pack(anchor='nw', fill='both', expand=1)
img_on_canvas = canvas.create_image(0, 0, image=new_image, anchor='nw')

##--------------------------Right Side-------------------------##
##--------------------------Right Top 1 Frame-------------------------##

assessment_label = Label(top1_right_frame, text="Dates Assessment Before Cutting: ", font='sans 10', bg='white')
assessment_label.grid(row=0, column=0, pady=10)

assessment_before = random.randint(3000, 5000)
assessment_before_label = Label(top1_right_frame, text=str(assessment_before), font='sans 10 bold', bg='white')
assessment_before_label.grid(row=0, column=1, pady=10)



##--------------------------Right Top 2 Frame-------------------------##

option_label = Label(top2_right_frame, text="Choose mode of operation:", bg='white')
option_label.grid(row=1, column=0, sticky="w", pady=10)

# Radio Buttons
r = StringVar()
r.set("None")

Radiobutton(top2_right_frame, text=" Manual marking", variable=r, value="Manual marking", command=lambda : clicked(r.get()), bg='white').grid(row=2, column=0, sticky="w")
Radiobutton(top2_right_frame, text=" Input of amount that will remain", variable=r, value="Input of amount", command=lambda : clicked(r.get()), bg='white').grid(row=4, column=0, sticky="w")

# Completed Drawing Button DISABLED
# b_done_draw = Button(top2_right_frame, text="Continue", command=done_drawing, state=DISABLED)
# b_done_draw.grid(row=3, column=0, padx=40, pady=10, sticky="w")

# Clear Drawing Button DISABLED
# b_clear_draw = Button(top2_right_frame, text="Clear Drawing", command=clear_drawing, state=DISABLED)
# b_clear_draw.grid(row=3, column=0, padx=40, pady=10, sticky="e")

# marking explain
marking_explain = Label(top2_right_frame, text="If you choose Manual marking, drow on\n"
                                               " the picture in the left side of the screen\n"
                                               " where is the line you want the mashine\n"
                                               " to cut the thinnig spot", font='sans 10', bg='white')
marking_explain.grid(row=3, column=0,pady=10, sticky='w')

# marking explain
input_explain = Label(top2_right_frame, text="Write A number: ", font='sans 10', bg='white')
input_explain.grid(row=5, column=0, padx=0,pady=10, sticky='w')
# Input Box DISABLED
ge = Entry(top2_right_frame, width=15, borderwidth=2, state=DISABLED)
ge.grid(row=5, column=0,pady=10, sticky="e")

# # Submit Button DISABLED
# b_submit = Button(top2_right_frame, text="Submit", command=submit_entry, state=DISABLED)
# b_submit.grid(row=6, column=0, padx=50, pady=5, sticky="w")

# Clear Entry Button DISABLED
# b_clear = Button(top2_right_frame, text="Clear", command=clear_entry, state=DISABLED)
# b_clear.grid(row=6, column=0, padx=50, pady=10, sticky="e")

# Selected String From Radio Buttons
selectedRadio = Label(top2_right_frame, text="Option Selected: ", font='sans 10', bg='white')
selectedRadio.grid(row=7, column=0, pady=5)
selectedRadioValue = Label(top2_right_frame, text=str(r.get()), font='sans 12 bold', bg='white')
selectedRadioValue.grid(row=8, column=0)

# Univarsal Continue button
b_submit = Button(top2_right_frame, text="Continue", command=univarsal_continue)
b_submit.grid(row=9, column=0, padx=50, pady=5, sticky="w")

# Univarsal Clear button
b_clear = Button(top2_right_frame, text="Clear", command=univarsal_clear)
b_clear.grid(row=9, column=0, padx=50, pady=10, sticky="e")


##--------------------------Right Top 3 Frame-------------------------##

L_length_range_label_text = Label(top3_right_frame, font='sans 10 bold', bg='white')
L_length_range_label = Label(top3_right_frame, padx=10, pady=10, font='sans 12 bold'
                             , bg='white', relief=GROOVE)
assessment_afterCut_label = Label(top3_right_frame, text="", font='sans 10', bg='white')
assessment_afterCut_label.grid(row=0, column=0, sticky="w", pady=5)
assessment_afterCut_num_label = Label(top3_right_frame, text="", font='sans 12 bold', bg='white')
assessment_afterCut_num_label.grid(row=0, column=1, sticky="w", pady=5)


##--------------------------Right Top 4 Frame-------------------------##
final_confirmation_helper = Label(top4_right_frame, bg='white')
final_confirmation_helper.pack(pady=20)
final_confirmation = Button(top4_right_frame, text="Cut", command=confirmation_click, padx=10,
                            font='sans 12 bold', bg="#FF0000", fg="white", state=DISABLED)
start_label = Label(frame_right, text="Welcome To\n\nDate Thinning User-Interface."
                    , font='sans 10 bold', bg='white')
start_label.pack(padx=29, pady=(200, 20), anchor=CENTER)
b_start_interface = Button(frame_right, text="Start", command=start_user_interface, padx=10,
                            font='sans 12 bold', bg="#228B22", fg="white")
b_start_interface.pack(pady=20, anchor=CENTER)


root.mainloop()
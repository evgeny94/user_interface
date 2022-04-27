import random, math
from tkinter import *
from tkinter.ttk import Separator
from PIL import ImageTk, Image
from tkinter import messagebox
import urllib.request
import os

root = Tk()
# root.title('User Interface')
root.resizable(False, False)
# turns off title bar, geometry
root.overrideredirect(True)

path1 = "C:/Date thinning/user_interface/images"
# Check whether the specified path exists or not
isExist = os.path.exists(path1)
print(isExist)
if isExist:
    pass
else:
    os.makedirs(path1, exist_ok=True)
    urllib.request.urlretrieve(
        'https://raw.githubusercontent.com/evgeny94/user_interface/master/images/icon.ico',
        "C:/Date thinning/user_interface/images/icon.ico")
    urllib.request.urlretrieve(
        'https://raw.githubusercontent.com/evgeny94/user_interface/master/images/palm1.jpg',
        "C:/Date thinning/user_interface/images/palm1.jpg")
    urllib.request.urlretrieve(
        'https://raw.githubusercontent.com/evgeny94/user_interface/master/images/palm3.JPG',
        "C:/Date thinning/user_interface/images/palm3.JPG")
    urllib.request.urlretrieve(
        'https://raw.githubusercontent.com/evgeny94/user_interface/master/images/palm4.png',
        "C:/Date thinning/user_interface/images/palm4.png")

def check_ifExist_image(filename):
    global palm_img, palm_img_san
    try:
        palm_img = Image.open(filename)
        palm_img_san = Image.open(filename)
        print("File accessible")
        return True
    except IOError:
        print("File not accessible")
        return False

def check_ifExist_icon(filename):
    global rib
    try:
        rib = root.iconbitmap(filename)
        print("File accessible")
        return True
    except IOError:
        print("File not accessible")
        return False

if check_ifExist_icon("C:/Date thinning/user_interface/images/icon.ico"):
    print("getting here?")
    pass
else:
    print("getting here?")
    root.iconbitmap('C:/Date thinning/user_interface/images/icon.ico')


## --------------- Screen configurations --------------- ##
screen_width = int(int(root.winfo_screenwidth())*0.92)
screen_height = int(int(root.winfo_screenheight())*0.9)
print("root managed: " + str(screen_width) + ", " + str(screen_height))

screen_width1 = root.winfo_screenwidth()
screen_height1 = root.winfo_screenheight()
print("root: " + str(screen_width1) + ", " + str(screen_height1))

root.state('zoomed')

## --------------- Frames --------------- ##
# make a frame for the title bar
title_bar = LabelFrame(root, bg='white', relief='raised', bd=2)
title_bar.grid(row=0, column=1, sticky="e", padx=5)
# put a close button on the title bar
close_button = Button(title_bar, text=' X ', command=root.destroy, font='sans 10')
close_button.pack(side=RIGHT)
title_label = Label(root, text="Date Thinning - User Interface", font='arial 11 bold')
title_label.grid(row=0, column=0, sticky="w", padx=5)

# Frame Creation Left
frame_left = LabelFrame(root, text="Picture", labelanchor='n', bg='white', font='sans 11 bold')
frame_left.grid(row=1, column=0, sticky="nsew")

# Frame Creation Right
frame_right = LabelFrame(root, text="Information", labelanchor='n', bg='white', font='sans 11 bold')
frame_right.grid(row=1, column=1, sticky="nsew")

# Frame Configuration Right
root.rowconfigure(index=0, weight=0)
root.rowconfigure(index=1, weight=150)
frame_right.rowconfigure(index=0, weight=0)
frame_right.rowconfigure(index=1, weight=1)
frame_right.rowconfigure(index=2, weight=1)
frame_right.rowconfigure(index=3, weight=0)

# Right Top 1 Frame
top1_right_frame = LabelFrame(frame_right, text="Assessment", labelanchor='n', bg='white', fg='#454545', font='sans 11 bold', borderwidth=4)

# Right Top 2 Frame
top2_right_frame = LabelFrame(frame_right, text="Operations", labelanchor='n', bg='white', fg='#454545', font='sans 11 bold', borderwidth=4)

# Right Top 3 Frame
top3_right_frame = LabelFrame(frame_right, labelanchor='n', bg='white', fg='#454545', font='sans 11 bold', borderwidth=4)
top3_right_frame.columnconfigure(index=0, weight=1)

# Right Top 4 Frame
top4_right_frame = LabelFrame(frame_right, labelanchor='n', bg='white', fg='#454545', font='sans 11 bold', borderwidth=4)

## --------------- Variables & Image --------------- ##
# For the submit button
num_clicked = 0

# Image + Configurations
img_selection = random.randint(1, 3)
print(img_selection)
if img_selection == 1:
    if check_ifExist_image("C:/Date thinning/user_interface/images/palm1.jpg"):
        pass
    else:
        palm_img = Image.open('C:/Date thinning/user_interface/images/palm1.jpg')
        palm_img_san = Image.open('C:/Date thinning/user_interface/images/palm1.jpg')
elif img_selection == 2:
    if check_ifExist_image("C:/Date thinning/user_interface/images/palm3.JPG"):
        pass
    else:
        palm_img = Image.open('C:/Date thinning/user_interface/images/palm3.JPG')
        palm_img_san = Image.open('C:/Date thinning/user_interface/images/palm3.JPG')
else:
    if check_ifExist_image("C:/Date thinning/user_interface/images/palm4.png"):
        pass
    else:
        palm_img = Image.open('C:/Date thinning/user_interface/images/palm4.png')
        palm_img_san = Image.open('C:/Date thinning/user_interface/images/palm4.png')

r_value = None
width_pre, heigth_pre, cnt = 0, 0, 0
width_pre_san, heigth_pre_san, cnt_san = 0, 0, 0
resized_image = palm_img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)
canvas = Canvas()
canvas_san = Canvas()
border_label = Label()

# Rectangle
width, height = canvas.winfo_width(), canvas.winfo_height()
if img_selection == 1:
    rec_x1, rec_y1 = int(width)*0.7, int(height)*0.25
    rec_x2, rec_y2 = int(width)*0.72, int(height)*0.45
    rel_x, rel_y = 0.73, 0.25
    o1, o2, R = round(int(width) * 0.532), round(int(height) * 0.924), round(int(height) * 0.642)
    angle_start, angle_end = 63, 155
elif img_selection == 2:
    rec_x1, rec_y1 = int(width) * 0.82, int(height) * 0.52
    rec_x2, rec_y2 = int(width) * 0.84, int(height) * 0.62
    rel_x, rel_y = 0.85, 0.52
    o1, o2, R = round(int(width)*0.319), round(int(height)*1.913), round(int(height)*1.579)
    angle_start, angle_end = 58, 104
else:
    rec_x1, rec_y1 = int(width)*0.84, int(height)*0.25
    rec_x2, rec_y2 = int(width)*0.865, int(height)*0.38
    rel_x, rel_y = 0.875, 0.25
    o1, o2, R = round(int(width)*0.584), round(int(height) * 1.117), round(int(height) * 0.899)
    angle_start, angle_end = 63, 140

def update_parameters():
    global border, zone, o1, o2, R
    width, height = canvas.winfo_width(), canvas.winfo_height()
    if img_selection == 1:
        border = int(width) * 0.41
        zone = border * 0.74
        o1, o2, R = round(int(width) * 0.532), round(int(height) * 0.924), round(int(height) * 0.642)
    elif img_selection == 2:
        border = int(width) * 0.46
        zone = border * 0.76
        o1, o2, R = round(int(width)*0.319), round(int(height)*1.913), round(int(height)*1.579)
    else:
        border = int(width) * 0.57
        zone = border * 0.81
        o1, o2, R = round(int(width)*0.584), round(int(height) * 1.117), round(int(height) * 0.899)

    print("border, zone: "+ str(border), str(zone))
    print("o1, o2, R = " + str(o1), str(o2), str(R))

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
    L_length_range_label_text.grid_forget()
    L_length_range_label.grid_forget()
    assessment_afterCut_label['text'] = ""
    assessment_afterCut_label['relief'] = FLAT
    top4_right_frame['text'] = ""
    final_confirmation.pack_forget()

def Show_2_last_frames():
    top3_right_frame['text'] = "Outcome"
    assessment_afterCut_label.grid(row=0, column=0, sticky="nsew", pady=5, columnspan=2)
    assessment_afterCut_num_label.grid(row=1, column=0, sticky="nsew", padx=50, pady=5, columnspan=2)
    L_length_range_label_text.grid(row=3, column=0, pady=5, sticky="nsew", columnspan=2)
    L_length_range_label.grid(row=4, column=0, padx=28, pady=5, sticky="nsew", columnspan=2)
    top4_right_frame['text'] = "Final confirmation"
    final_confirmation.pack(pady=10)
    final_confirmation_helper.pack_forget()

# --------------- Main Image Drawing ---------------
def create_square():
    global robot_start_square
    robot_start_label = Label(canvas, text="The Robot\n"
                                           "Starts Here", font='sans 10 bold', bg="black", fg="#00FFFF")
    robot_start_label.place(relx=rel_x, rely=rel_y)
    robot_start_square = canvas.create_rectangle(rec_x1, rec_y1, rec_x2, rec_y2, outline="#00FFFF", width=6, tags='startsqaure')

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
    assessment_afterCut_label['relief'] = FLAT
    assessment_afterCut_num_label['text'] = ""
    assessment_afterCut_num_label['relief'] = FLAT
    assessment_afterCut_num_label['bg'] = 'white'
    final_confirmation['state'] = DISABLED
    b_submit['state'] = DISABLED
    b_redraw['state'] = NORMAL
    b_redraw['bg'] = '#4B0082'
    b_redraw['fg'] = 'white'
    canvas.bind("<Button-1>", get_xy)
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<B1-ButtonRelease>", doneStroke)

def doneStroke(event):
    global line
    line = canvas.itemconfigure('currentline', width=8)
    print('Canvas coords:' + str(canvas.coords('currentline')))
    b_submit['state'] = NORMAL
    b_submit['bg'] = 'green'
    b_submit['fg'] = 'white'

def create_random_line(assessment):
    global line

    blocks = round(assessment_before / 3)
    print(blocks)
    if img_selection == 1:
        if assessment > 0 and assessment < blocks:
            x1, y1, x2, y2 = random.randint(187, 235), random.randint(56, 124), \
                             random.randint(427, 511), random.randint(483, 560)
            line = canvas.create_line(x1, y1, x2, y2, fill="#00FFFF", width=8, tags='randomcurrentline')
        elif assessment >= blocks and assessment < 2*blocks:
            x1, y1, x2, y2 = random.randint(70, 105), random.randint(92, 148), \
                             random.randint(373, 425), random.randint(565, 665)
            line = canvas.create_line(x1, y1, x2, y2, fill="#00FFFF", width=8, tags='randomcurrentline')
        else:
            x1, y1, x2, y2 = random.randint(14, 97), random.randint(242, 350), \
                             random.randint(389, 430), random.randint(655, 742)
            line = canvas.create_line(x1, y1, x2, y2, fill="#00FFFF", width=8, tags='randomcurrentline')
    elif img_selection == 2:
        if assessment > 0 and assessment < blocks:
            x1, y1, x2, y2 = random.randint(385, 460), random.randint(70, 95), \
                             random.randint(430, 495), random.randint(550, 620)
            line = canvas.create_line(x1, y1, x2, y2, fill="#00FFFF", width=8, tags='randomcurrentline')
        elif assessment >= blocks and assessment < 2*blocks:
            x1, y1, x2, y2 = random.randint(250, 355), random.randint(75, 90), \
                             random.randint(310, 430), random.randint(665, 720)
            line = canvas.create_line(x1, y1, x2, y2, fill="#00FFFF", width=8, tags='randomcurrentline')
        else:
            x1, y1, x2, y2 = random.randint(130, 245), random.randint(100, 114), \
                             random.randint(310, 355), random.randint(690, 725)
            line = canvas.create_line(x1, y1, x2, y2, fill="#00FFFF", width=8, tags='randomcurrentline')
    else:
        if assessment > 0 and assessment < blocks:
            x1, y1, x2, y2 = random.randint(515, 615), random.randint(30, 35), \
                             random.randint(660, 735), random.randint(485, 585)
            line = canvas.create_line(x1, y1, x2, y2, fill="#00FFFF", width=8, tags='randomcurrentline')
        elif assessment >= blocks and assessment < 2*blocks:
            x1, y1, x2, y2 = random.randint(380, 515), random.randint(30, 40), \
                             random.randint(560, 660), random.randint(485, 770)
            line = canvas.create_line(x1, y1, x2, y2, fill="#00FFFF", width=8, tags='randomcurrentline')
        else:
            x1, y1, x2, y2 = random.randint(265, 370), random.randint(30, 70), \
                             random.randint(450, 560), random.randint(500, 770)
            line = canvas.create_line(x1, y1, x2, y2, fill="#00FFFF", width=8, tags='randomcurrentline')


def end_spikelet_window():
    global myArc
    width, height = canvas.winfo_width(), canvas.winfo_height()
    width_pre_4_san, height_pre_4_san = canvas_san.winfo_width(), canvas_san.winfo_height()
    x_arc_san = [point_san[0] for point_san in points_san]
    y_arc_san = [point_san[1] for point_san in points_san]
    x_arc_san_0, y_arc_san_0 = x_arc_san[0], y_arc_san[0]
    x_arc_san_0, y_arc_san_0 = float(round((x_arc_san_0 / width_pre_4_san) * width)), \
                               float(round((y_arc_san_0 / height_pre_4_san) * height))
    x_arc_san_last, y_arc_san_last = x_arc_san[-1], y_arc_san[-1]
    x_arc_san_last, y_arc_san_last = float(round((x_arc_san_last / width_pre_4_san) * width)), \
                                     float(round((y_arc_san_last / height_pre_4_san) * height))
    print("x_arc_san_0, y_arc_san_0, x_arc_san_last, y_arc_san_last: " + str(x_arc_san_0), str(y_arc_san_0)
          , str(x_arc_san_last), str(y_arc_san_last))
    if img_selection == 1:
        myArc = canvas.create_arc(x_arc_san[0], y_arc_san[0], x_arc_san[-1], y_arc_san[-1],
                                      start=63,
                                      extent=92,
                                      style=ARC,
                                      outline="#4B0082",
                                      width=8,
                                      tags='manualArcSan')
    elif img_selection == 2:
        myArc = canvas.create_arc(x_arc_san[0], y_arc_san[0], x_arc_san[-1], y_arc_san[-1],
                                      start=30,
                                      extent=110,
                                      style=ARC,
                                      outline="#4B0082",
                                      width=8,
                                      tags='manualArcSan')
    else:
        myArc = canvas.create_arc(x_arc_san[0], y_arc_san[0], x_arc_san[-1], y_arc_san[-1],
                                      start=63,
                                      extent=92,
                                      style=ARC,
                                      outline="#4B0082",
                                      width=8,
                                      tags='manualArcSan')
    coord0, coord1, coord2, coord3 = int(canvas_san.coords('manualArcSan')[0]), int(canvas_san.coords('manualArcSan')[1]), \
                                     int(canvas_san.coords('manualArcSan')[2]), int(canvas_san.coords('manualArcSan')[3])
    coord0, coord1, coord2, coord3 = float(round((coord0 / width_pre_4_san) * width)), \
                                     float(round((coord1 / height_pre_4_san) * height)), \
                                     float(round((coord2 / width_pre_4_san) * width)), \
                                     float(round((coord3 / height_pre_4_san) * height))
    canvas.coords('manualArcSan', coord0, coord1, coord2, coord3)
    Spikelet_Window.destroy()

    if r_value == None:
        canvas.bind("<Button-1>", 'none')
        canvas.bind("<B1-Motion>", 'none')
        canvas.bind("<B1-ButtonRelease>", 'none')

# --------------- Spiklet Drawing ---------------
def get_xy_san(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def clear_drawing_san():
    global canvas_san, line_san
    canvas_san.delete('line_san')
    canvas_san.delete('manualArcSan')
    quit_button['state'] = DISABLED
    quit_button['bg'] = '#f0f0f0'
    quit_button['fg'] = 'black'

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
    if img_selection == 1:
        myArc = canvas_san.create_arc(x_arc_san[0], y_arc_san[0], x_arc_san[-1], y_arc_san[-1],
                                    start=63,
                                    extent=92,
                                    style=ARC,
                                    outline="#4B0082",
                                    width=8,
                                    tags='manualArcSan')
    elif img_selection == 2:
        myArc = canvas_san.create_arc(x_arc_san[0], y_arc_san[0], x_arc_san[-1], y_arc_san[-1],
                                      start=30,
                                      extent=110,
                                      style=ARC,
                                      outline="#4B0082",
                                      width=8,
                                      tags='manualArcSan')
    else:
        myArc = canvas_san.create_arc(x_arc_san[0], y_arc_san[0], x_arc_san[-1], y_arc_san[-1],
                                      start=63,
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
    quit_button['state'] = NORMAL
    quit_button['bg'] = 'green'
    quit_button['fg'] = 'white'
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

    resized_image_san = palm_img_san.resize((width_san, heigth_san), Image.Resampling.LANCZOS)
    new_image_san = ImageTk.PhotoImage(resized_image_san)
    canvas_san.itemconfig(img_on_canvas_san, image=new_image_san)

# In case the Leading Spikelet not found
def manual_spikelet_drawing():
    global canvas_san, final_confirmation, Spikelet_Window, img_on_canvas_san, quit_button, found, b_redraw, exp_label_san_win
    # Disabling Cut Button
    final_confirmation['state'] = DISABLED
    b_submit['state'] = DISABLED

    # Open new window for drawing the spikelet
    Spikelet_Window = Toplevel()
    Spikelet_Window.title('Marking The Leading Spikelet Manually')
    Spikelet_Window.attributes('-fullscreen', True)
    # Left Frame
    left_main_frame = LabelFrame(Spikelet_Window, text="Picture", labelanchor='n', bg="white", font='sans 10 bold')
    left_main_frame.grid(row=0, column=0, sticky="nsew")

    # Right Frame
    right_frame = LabelFrame(Spikelet_Window, text="Information", labelanchor='n', bg="white", font='sans 10 bold')
    right_frame.grid(row=0, column=1, sticky="nsew")

    right_top_frame = LabelFrame(right_frame, text="Instructions", labelanchor='n', bg="white", fg='#454545', font='sans 10 bold', borderwidth=3)
    right_top_frame.grid(row=0, column=0, sticky="nsew", pady=(125, 100))

    right_bottom_frame = LabelFrame(right_frame, text="Buttons", labelanchor='n', bg="white", fg='#454545', font='sans 10 bold', borderwidth=3)
    right_bottom_frame.grid(row=1, column=0, sticky="nsew")

    # Grid configuration
    Grid.rowconfigure(Spikelet_Window, index=0, weight=2)
    Grid.columnconfigure(Spikelet_Window, index=0, weight=2)

    # Frame configuration
    left_main_frame.rowconfigure(index=0, weight=2)
    left_main_frame.columnconfigure(index=0, weight=2)

    # right_frame.rowconfigure(index=0, weight=1)
    # right_frame.rowconfigure(index=1, weight=1)
    right_frame.columnconfigure(index=0, weight=1)

    right_bottom_frame.columnconfigure(index=0, weight=1)
    right_bottom_frame.rowconfigure(index=0, weight=1)

    # Canvas
    canvas_san = Canvas(left_main_frame, bg="white")
    canvas_san.pack(anchor='nw', fill='both', expand=1)
    img_on_canvas_san = canvas_san.create_image(0, 0, image=new_image, anchor='nw')

    # Enable Drawing
    canvas_san.bind("<B1-Motion>", motion_san)
    canvas_san.bind("<ButtonRelease-1>", on_click_release_san)
    Spikelet_Window.bind("<Button-3>", get_xy_san)
    Spikelet_Window.bind("<B3-Motion>", move_san)

    # Explain Functionality
    mouse_use_label = Label(right_top_frame, text="Draw the leading spikelet \nusing your mouse:", bg="white", font='sans 13 bold')
    mouse_use_label.grid(row=0, column=0, pady=5)

    separator = Separator(right_top_frame, orient='horizontal')
    separator.grid(row=1, column=0, sticky='nsew')
    global exp_label_san_win_left, exp_label_san_win_right
    exp_label_san_win_left = Label(right_top_frame, text="Left button - Draw", bg="#CAFF70",
                                   relief=RIDGE, font='sans 11 bold')
    exp_label_san_win_left.grid(row=2, column=0, padx=5, pady=5, sticky='w')

    exp_label_san_win_right = Label(right_top_frame, text="Right button - Move Drawing", bg="#CAFF70",
                                   relief=RIDGE, font='sans 11 bold')
    exp_label_san_win_right.grid(row=3, column=0, padx=5, pady=5, sticky='w')


    # Exit button
    quit_button = Button(right_bottom_frame, text="Save and Continue", command=end_spikelet_window, state=DISABLED, font='sans 11 bold')
    quit_button.grid(row=0, column=0, padx=(5, 70), pady=5, sticky='nw')

    # Clear button
    clear_button = Button(right_bottom_frame, text="Clear", command=clear_drawing_san, font='sans 11 bold')
    clear_button.grid(row=0, column=0, padx=(70, 5), pady=5, sticky='ne')

    # Hook window size changes
    Spikelet_Window.bind('<Configure>', size_changed_san)
    Spikelet_Window.state('zoomed')
    b_redraw['text'] = "Redraw leading spikelet"
    Spikelet_Window.after(1500, flash, 0)

def flash(count):
    global exp_label_san_win_left, exp_label_san_win_right
    if count%2 == 0:
        exp_label_san_win_left.configure(background='green', foreground='white')
        exp_label_san_win_right.configure(background='green', foreground='white')
    else:
        exp_label_san_win_left.configure(background='#CAFF70', foreground='black')
        exp_label_san_win_right.configure(background='#CAFF70', foreground='black')
    count += 1
    if (count < 6):
        Spikelet_Window.after(700, flash, count)

def clicked(value):
    global ge, b_submit, b_clear, b_redraw, b_clear_draw, final_confirmation, assessment_afterCut_label, assessment_afterCut_num_label, r_value, b_radio1, b_radio2, border_label, border
    if len(canvas.coords('manualArcSan')) == 0 and len(canvas.coords('currentArc')) == 0:
        start_spikelet_configuration()
    r_value = value
    final_confirmation['state'] = DISABLED
    b_clear['state'] = NORMAL
    if value == "Input of amount":
        # Clear and Disable Drawing
        clear_drawing()
        canvas.delete('border_line')
        border_label.destroy()
        canvas.bind("<Button-1>", 'none')
        canvas.bind("<B1-Motion>", 'none')
        canvas.bind("<B1-ButtonRelease>", 'none')
        root.bind('<Return>', enter_pressed)
        root.bind("<BackSpace>", check_entry)
        root.bind("<Delete>", check_entry)
        b_submit['state'] = NORMAL
        b_redraw['state'] = NORMAL
        b_submit['bg'] = '#f0f0f0'
        b_submit['fg'] = 'black'
        b_redraw['bg'] = '#4B0082'
        b_redraw['fg'] = 'white'

        # Hide 2 last frames
        Hide_2_last_frames()

        # Entry
        ge['state'] = NORMAL
        ge.focus()

        b_radio1['bg'], b_radio2['bg'] = 'white', '#CAFF70'
        marking_explain['bg'], input_explain['bg'] = 'white', '#CAFF70'
        b_radio1['relief'], b_radio2['relief'] = RAISED, RIDGE
        marking_explain['relief'], input_explain['relief'] = FLAT, RIDGE

    else:
        # Forget previous assessment and drawings
        assessment_afterCut_label['text'] = ""
        assessment_afterCut_label['relief'] = FLAT
        assessment_afterCut_num_label['text'] = ""
        assessment_afterCut_num_label['relief'] = FLAT
        assessment_afterCut_num_label['bg'] = 'white'
        canvas.delete('randomcurrentline')

        # Enable Drawing
        canvas.bind("<Button-1>", get_xy)
        canvas.bind("<B1-Motion>", draw)
        canvas.bind("<B1-ButtonRelease>", doneStroke)
        root.bind('<Return>', 'none')
        root.bind("<BackSpace>", 'none')
        root.bind("<Delete>", 'none')

        # Border Line + Label
        update_parameters()
        print(border)
        canvas.create_line(border, 0, border, canvas.winfo_height(), fill="black", dash=(50, 10), width=6, tags='border_line')
        border_label = Label(canvas, text="Fruitlets zone", font='sans 13 bold', bg='#CAFF70', relief=RIDGE)
        border_label.place(x=zone, y=3)


        #Hide 2 last frames
        Hide_2_last_frames()

        # Entry DISABLED & Clear
        ge.delete(0, END)
        ge['state'] = DISABLED

        b_radio1['bg'], b_radio2['bg'] = '#CAFF70', 'white'
        marking_explain['bg'], input_explain['bg'] = '#CAFF70', 'white'
        b_radio1['relief'], b_radio2['relief'] = RIDGE, RAISED
        marking_explain['relief'], input_explain['relief'] = RIDGE, FLAT

        b_submit['state'] = DISABLED
        b_redraw['state'] = NORMAL
        b_redraw['bg'] = '#4B0082'
        b_redraw['fg'] = 'white'

def range_calculator(str_opr, assessment):
    blocks = round(assessment_before / 3)
    if str_opr == 'number':
        if assessment > 0 and assessment < blocks:
            return random.randint(50, 60)
        elif assessment >= blocks and assessment < 2 * blocks:
            return random.randint(61, 70)
        else:
            return random.randint(71, 80)
    else:
        coord1, coord2, coord3, coord4 = assessment[0], assessment[1], assessment[2], assessment[3]
        avg_x, avg_y = (coord1+coord3)/2, (coord2+coord4)/2
        if img_selection == 1:
            if avg_x <= border and avg_x > 360:
                return random.randint(50, 60)
            elif avg_x <= 360 and avg_x > 265:
                return random.randint(61, 70)
            elif avg_x <= 265 and avg_x >= 120:
                return random.randint(71, 80)
            else:
                return None
        elif img_selection == 2:
            if avg_x <= border and avg_x > 430:
                return random.randint(50, 60)
            elif avg_x <= 430 and avg_x > 300:
                return random.randint(61, 70)
            elif avg_x <= 300 and avg_x >= 100:
                return random.randint(71, 80)
            else:
                return None
        else:
            if avg_x <= border and avg_x > 578:
                return random.randint(50, 60)
            elif avg_x <= 578 and avg_x > 466:
                return random.randint(61, 70)
            elif avg_x <= 466 and avg_x >= 365:
                return random.randint(71, 80)
            else:
                return None

def clear_entry():
    global assessment_afterCut_label, assessment_afterCut_num_label, L_length_range_label_text, L_length_range_label, num_clicked, final_confirmation

    ge.delete(0, END)
    canvas.delete('randomcurrentline')
    num_clicked = 0
    Hide_2_last_frames()
    assessment_afterCut_label['text'] = ""
    assessment_afterCut_label['relief'] = FLAT
    assessment_afterCut_num_label['text'] = ""
    assessment_afterCut_num_label['relief'] = FLAT
    assessment_afterCut_num_label['bg'] = 'white'
    b_submit['state'] = NORMAL
    b_redraw['state'] = NORMAL
    b_redraw['bg'] = '#4B0082'
    b_redraw['fg'] = 'white'
    root.bind('<Return>', enter_pressed)

    # Disabling Cut Button
    final_confirmation['state'] = DISABLED

def submit_restart():
    global assessment_afterCut_label, assessment_afterCut_num_label, L_length_range_label_text, L_length_range_label, final_confirmation, b_submit

    assessment_afterCut_label['text'] = ""
    assessment_afterCut_label['relief'] = FLAT
    assessment_afterCut_num_label['text'] = ""
    assessment_afterCut_num_label['relief'] = FLAT
    assessment_afterCut_num_label['bg'] = 'white'
    L_length_range_label_text['state'] = NORMAL
    L_length_range_label_text['relief'] = FLAT
    L_length_range_label['state'] = NORMAL
    b_submit['state'] = NORMAL
    b_redraw['state'] = NORMAL
    b_redraw['bg'] = '#4B0082'
    b_redraw['fg'] = 'white'
    canvas.delete('randomcurrentline')
    # Disabling Cut Button
    final_confirmation['state'] = DISABLED

def submit_entry():
    global ge, new_image, L_length_range_label_text, assessment_afterCut_label, assessment_afterCut_num_label, num_clicked, final_confirmation, b_submit

    valid = ge.get().isdigit()
    # Number of clicks on submit for deleting previous grids
    # First time clicked
    if valid == True:
        if int(ge.get()) == 0:
            clear_entry()
            messagebox.showerror("Entry Box Error",
                                     "Try a number greater than 0.")
        elif int(ge.get()) < assessment_before:
            if num_clicked == 1:
                Show_2_last_frames()
                assessment_afterCut_label['text'] = "Expected remaining fruitlets:"
                assessment_afterCut_label['relief'] = GROOVE
                assessment_afterCut_num_label['text'] = str(int(ge.get()) + random.randint(-50, 50))
                assessment_afterCut_num_label['relief'] = GROOVE
                assessment_afterCut_num_label['bg'] = '#CAFF70'
                L_length_range_label_text['text'] = "Spikelets remaining length:"
                L_length_range_label_text['relief'] = GROOVE
                L_length_range_label['text'] = str(range_calculator('number', int(ge.get()))) + " cm"

                # Enabling Cut Button
                final_confirmation['state'] = NORMAL

                # Random Line
                create_random_line(int(ge.get()))
                b_submit['state'] = DISABLED
                b_redraw['state'] = DISABLED
                b_redraw['bg'] = '#f0f0f0'
                b_redraw['fg'] = 'black'
                root.bind('<Return>', 'none')
            # Already clicked
            else:
                submit_restart()
                Show_2_last_frames()
                assessment_afterCut_label['text'] = "Expected remaining fruitlets:"
                assessment_afterCut_label['relief'] = GROOVE
                assessment_afterCut_num_label['text'] = str(int(ge.get()) + random.randint(0, 75))
                assessment_afterCut_num_label['relief'] = GROOVE
                assessment_afterCut_num_label['bg'] = '#CAFF70'
                L_length_range_label_text['text'] = "Spikelets remaining length:"
                L_length_range_label_text['relief'] = GROOVE
                L_length_range_label['text'] = str(range_calculator('number', int(ge.get()))) + " cm"
                # Enabling Cut Button
                final_confirmation['state'] = NORMAL
                # Random Line
                create_random_line(int(ge.get()))
                b_submit['state'] = DISABLED
                b_redraw['state'] = DISABLED
                b_redraw['bg'] = '#f0f0f0'
                b_redraw['fg'] = 'black'
                root.bind('<Return>', 'none')
        else:
            clear_entry()
            messagebox.showerror("Entry Box Error", "The number is equal or greater than the initial assessment!\nPlease try again.")
    else:
        if ge.get() == "":
            messagebox.showerror("Entry Box Error",
                                 "The Entry Box is empty!\nPlease fill it in first.")
        else:
            clear_entry()
            messagebox.showerror("Entry Box Error", "This Entry Box may contain only digits and positive numbers!\nPlease try again.")

def confirmation_click():
    global assessment_afterCut_num_label, L_length_range_label
    # Confirmation_Window = Toplevel(root)
    # Confirmation_Window.title('Final confirmation')
    # text_label1 = Label(Confirmation_Window, text="There is no way back from here.\n\n", font='sans 15 bold')
    # text_label2 = Label(Confirmation_Window, text="Summary\n", font='sans 14 bold')
    # text_label3 = Label(Confirmation_Window, text="Expected remaining fruitlets: " + str(assessment_afterCut_num_label) + "\n", font='sans 11 bold')
    # text_label4 = Label(Confirmation_Window, text="Spikelets remaining length: " + str(L_length_range_label) + "\n\n", font='sans 11 bold')
    # text_label5 = Label(Confirmation_Window, text="Execute cut?"+ "\n\n", font='sans 12 bold')
    # text_label1.pack()
    # text_label2.pack()
    # text_label3.pack()
    # text_label4.pack()
    # text_label5.pack()

    confirmation_respond = messagebox.askyesno("Final confirmation", "There is no way back from here.\n\n"
                                                                     "Execute cut?")
    if confirmation_respond == 1:
        root.destroy()
    else:
        return

def afterCut_calculator(assessment):
    global border
    coord1, coord2, coord3, coord4 = assessment[0], assessment[1], assessment[2], assessment[3]
    avg_x, avg_y = (coord1 + coord3) / 2, (coord2 + coord4) / 2
    blocks = round(assessment_before / 3)
    if img_selection == 1:
        if avg_x <= border and avg_x > 360:
            return random.randint(0, blocks)
        elif avg_x <= 360 and avg_x > 265:
            return random.randint(blocks, blocks*2)
        elif avg_x <= 265 and avg_x >= 120:
            return random.randint(blocks*2, assessment_before)
        else:
            return None
    elif img_selection == 2:
        if avg_x <= border and avg_x > 430:
            return random.randint(0, blocks)
        elif avg_x <= 430 and avg_x > 280:
            return random.randint(blocks, blocks*2)
        elif avg_x <= 280 and avg_x >= 130:
            return random.randint(blocks*2, assessment_before)
        else:
            return None
    else:
        if avg_x <= border and avg_x > 578:
            return random.randint(0, blocks)
        elif avg_x <= 578 and avg_x > 466:
            return random.randint(blocks, blocks*2)
        elif avg_x <= 466 and avg_x >= 365:
            return random.randint(blocks*2, assessment_before)
        else:
            return None

def done_drawing():
    global canvas, assessment_afterCut_num_label, L_length_range_label

    ans_afterCut_assessment = afterCut_calculator(canvas.coords('currentline'))
    ans_afterCut_length = range_calculator('line', canvas.coords('currentline'))
    if ans_afterCut_length != None and ans_afterCut_assessment != None:
        assessment_afterCut_label['text'] = "Expected remaining fruitlets:"
        assessment_afterCut_label['relief'] = GROOVE
        assessment_afterCut_num_label['text'] = str(ans_afterCut_assessment)
        assessment_afterCut_num_label['relief'] = GROOVE
        assessment_afterCut_num_label['bg'] = '#CAFF70'
        L_length_range_label_text['text'] = "Spikelets remaining length:"
        L_length_range_label_text['relief'] = GROOVE
        L_length_range_label['text'] = str(ans_afterCut_length) + " cm"
        # Enabling Cut Button
        final_confirmation['state'] = NORMAL
        b_submit['state'] = DISABLED
        b_submit['bg'] = '#f0f0f0'
        b_submit['fg'] = 'black'
        b_redraw['state'] = DISABLED
        b_redraw['bg'] = '#f0f0f0'
        b_redraw['fg'] = 'black'
        canvas.bind("<Button-1>", 'none')
        canvas.bind("<B1-Motion>", 'none')
        canvas.bind("<B1-ButtonRelease>", 'none')
        Show_2_last_frames()
    else:
        Hide_2_last_frames()
        canvas.delete('currentline')
        messagebox.showwarning("Drawing Error", "Draw only on the fruitlets zone.")

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

def redraw_rectangle():
    global canvas, rec_x1, rec_y1, rec_x2, rec_y2
    width, height = canvas.winfo_width(), canvas.winfo_height()

    print("startsqaure.coords: " + str(canvas.coords('startsqaure')))
    if cnt > 1 and len(canvas.coords("startsqaure")) != 0:
        if img_selection == 1:
            new_rec_x1, new_rec_y1 = int(width) * 0.7, int(height) * 0.25
            new_rec_x2, new_rec_y2 = int(width)*0.72, int(height)*0.45
            canvas.coords('startsqaure', new_rec_x1, new_rec_y1, new_rec_x2, new_rec_y2)
            print("startsqaure.coords after: " + str(canvas.coords('startsqaure')))
        elif img_selection == 2:
            new_rec_x1, new_rec_y1 = int(width) * 0.82, int(height) * 0.52
            new_rec_x2, new_rec_y2 = int(width) * 0.84, int(height) * 0.62
            canvas.coords('startsqaure', new_rec_x1, new_rec_y1, new_rec_x2, new_rec_y2)
            print("startsqaure.coords after: " + str(canvas.coords('startsqaure')))
        else:
            new_rec_x1, new_rec_y1 = int(width) * 0.84, int(height) * 0.25
            new_rec_x2, new_rec_y2 = int(width) * 0.865, int(height) * 0.38
            canvas.coords('startsqaure', new_rec_x1, new_rec_y1, new_rec_x2, new_rec_y2)
            print("startsqaure.coords after: " + str(canvas.coords('startsqaure')))
    else:
        pass

def redraw_arc():
    global canvas, R, o1, o2, found
    width, heigth = canvas.winfo_width(), canvas.winfo_height()
    if found == True and len(points_san) == 0:
        print("width, heigth:" + str(width), str(heigth))
        if width_pre_4_line > 1 and height_pre_4_line > 1:
            canvas.delete('currentArc')
            update_parameters()
            camvas_arc = canvas.create_circle_arc(o1, o2, R, style="arc", outline="#4B0082", width=8,
                                                  start=angle_start, end=angle_end, tags='currentArc') #what happend here?
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
            if img_selection == 1:
                myArc = canvas_san.create_arc(x_arc_san[0], y_arc_san[0], x_arc_san[-1], y_arc_san[-1],
                                              start=63,
                                              extent=92,
                                              style=ARC,
                                              outline="#4B0082",
                                              width=8,
                                              tags='manualArcSan')
            elif img_selection == 2:
                myArc = canvas_san.create_arc(x_arc_san[0], y_arc_san[0], x_arc_san[-1], y_arc_san[-1],
                                              start=30,
                                              extent=110,
                                              style=ARC,
                                              outline="#4B0082",
                                              width=8,
                                              tags='manualArcSan')
            else:
                myArc = canvas_san.create_arc(x_arc_san[0], y_arc_san[0], x_arc_san[-1], y_arc_san[-1],
                                              start=63,
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
        width_pre, heigth_pre = width, heigth
        size(event)
    else:
        pass

def size(event):
    global new_image, resized_image, canvas

    width, heigth = canvas.winfo_width(), canvas.winfo_height()
    print('Canvas size:', width, 'x', heigth)

    resized_image = palm_img.resize((width, heigth), Image.Resampling.LANCZOS)
    new_image = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(img_on_canvas, image=new_image)
    # redraw_line()
    # redraw_arc()
    redraw_rectangle()

def start_spikelet_configuration():
    global found, b_redraw, o1, o2, R

    update_parameters()
    if found == True:
        # camvas_arc = canvas.create_circle_arc(o1, o2, R, style="arc", outline="#4B0082", width=8,
        #                                       start=angle_start, end=angle_end, tags='currentArc')
        pass
    else:
        messagebox.showinfo("Information regards the <Leading Spikelet>",
                            "<Leading Spikelet> has not been found."
                            "\n\nPlease draw one manually.")
        manual_spikelet_drawing()

def start_user_interface():
    global found, b_redraw
    b_start_interface.pack_forget()
    start_label.pack_forget()
    update_parameters()
    # Right Top 1 Frame
    top1_right_frame.grid(row=0, column=0, sticky="nsew")
    top1_right_frame.grid_columnconfigure(index=0, weight=1)
    # Right Top 2 Frame
    top2_right_frame.grid(row=1, column=0, sticky="nsew")

    # Right Top 3 Frame
    top3_right_frame.grid(row=2, column=0, sticky="nsew")

    # Right Top 4 Frame
    top4_right_frame.grid(row=3, column=0, sticky="nsew")

    # Does the calculating system found a leading spikelet
    found = found_leading_sansun()

    # Robot's Location
    create_square()

    # Redraw Leading Spikelet
    if found == True:
        camvas_arc = canvas.create_circle_arc(o1, o2, R, style="arc", outline="#4B0082", width=8,
                                              start=angle_start, end=angle_end, tags='currentArc')
        b_redraw = Button(top2_right_frame, text="Redraw leading spikelet", font='sans 11 bold', bg="#4B0082", fg="white", command=redraw_leading_spikelet, anchor=CENTER)
    else:
        b_redraw = Button(top2_right_frame, text="Draw leading spikelet", font='sans 10 bold', bg="#4B0082", fg="white", command=redraw_leading_spikelet, anchor=CENTER)
    b_redraw.grid(row=0, column=0, pady=10, columnspan=2)

def redraw_leading_spikelet():
    canvas.delete('currentArc')
    canvas.delete('manualArcSan')
    b_submit['state'] = DISABLED
    b_submit['bg'] = '#f0f0f0'
    b_submit['fg'] = 'black'
    clear_drawing()
    clear_entry()
    manual_spikelet_drawing()

def enter_pressed(e):
    submit_entry()

def check_entry(e):
    if ge.get() == "":
        clear_entry()

def univarsal_continue():
    global r_value
    if r_value == "Input of amount":
        submit_entry()
    else:
        done_drawing()


def univarsal_clear():
    global r_value
    b_submit['bg'] = '#f0f0f0'
    b_submit['fg'] = 'black'
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

assessment_label = Label(top1_right_frame, text="Fruitlets:", font='sans 12 bold', bg='white')
assessment_label.grid(row=0, column=0, padx=5, pady=10, sticky='w')

assessment_before = random.randint(3000, 5000)
assessment_before_label = Label(top1_right_frame, text=str(assessment_before), font='sans 12 bold', relief=GROOVE, bg='#CAFF70')
assessment_before_label.grid(row=0, column=1, padx=10, pady=10)

##--------------------------Right Top 2 Frame-------------------------##

option_label = Label(top2_right_frame, text="Choose mode of operation:", font='sans 11 bold', bg='white', relief=GROOVE)
option_label.grid(row=1, column=0, sticky="nsew", pady=10)

# Radio Buttons
r = StringVar()
r.set("None")

b_radio1 = Radiobutton(top2_right_frame, text=" Manual marking", font='sans 11 bold', relief=RAISED, variable=r, value="Manual marking", command=lambda : clicked(r.get()), bg='white')
b_radio2 = Radiobutton(top2_right_frame, text=" Input of amount\n(that will remain)", font='sans 11 bold', relief=RAISED, variable=r, value="Input of amount", command=lambda : clicked(r.get()), bg='white')

b_radio1.grid(row=2, column=0)
separator1 = Separator(top2_right_frame, orient='horizontal')
separator1.grid(row=4, column=0, sticky='nsew', pady=(0, 15))
b_radio2.grid(row=5, column=0, padx=5)

# marking explain
marking_explain = Label(top2_right_frame, text="* Using the left mouse button,\ndraw a line.",
                        font='sans 12', bg='white')
marking_explain.grid(row=3, column=0, pady=10, sticky='nsew')

# marking explain
input_explain = Label(top2_right_frame, text="* Type in a number: ", font='sans 12', bg='white')
input_explain.grid(row=6, column=0, padx=(0, 110), pady=10, sticky='nsew')
# Input Box DISABLED
ge = Entry(top2_right_frame, width=10, borderwidth=2, font='sans 11 bold', state=DISABLED)
ge.grid(row=6, column=0, padx=10, pady=15, sticky="e")

# separator2 = Separator(top2_right_frame, orient='horizontal')
# separator2.grid(row=7, column=0, sticky='nsew')
# Univarsal Continue button
b_submit = Button(top2_right_frame, text="Continue", font='sans 11 bold', command=univarsal_continue, state=DISABLED)
b_submit.grid(row=8, column=0, padx=50, pady=5, sticky="w")

# Univarsal Clear button
b_clear = Button(top2_right_frame, text="Clear", font='sans 11 bold', command=univarsal_clear, state=DISABLED)
b_clear.grid(row=8, column=0, padx=50, pady=10, sticky="e")

##--------------------------Right Top 3 Frame-------------------------##

assessment_afterCut_label = Label(top3_right_frame, text="", font='sans 11 bold', bg='white')
assessment_afterCut_num_label = Label(top3_right_frame, padx=5, pady=5, text="", font='sans 12 bold', bg='white'
                                      , relief=GROOVE)

L_length_range_label_text = Label(top3_right_frame, text="", font='sans 11 bold', bg='white')
L_length_range_label = Label(top3_right_frame, padx=5, pady=5, font='sans 12 bold', bg='#CAFF70'
                             , relief=GROOVE)

##--------------------------Right Top 4 Frame-------------------------##
final_confirmation_helper = Label(top4_right_frame, bg='white')
final_confirmation_helper.pack(pady=20)
final_confirmation = Button(top4_right_frame, text="Thin", command=confirmation_click, padx=10,
                            font='sans 15 bold', bg="#FF0000", fg="white", state=DISABLED)
start_label = Label(frame_right, text="Welcome To\n\nDate Thinning User-Interface."
                    , font='sans 12 bold', bg='white')
start_label.pack(padx=15, pady=(200, 20), anchor=CENTER)
b_start_interface = Button(frame_right, text="Start", command=start_user_interface, padx=10,
                            font='sans 15 bold', bg="#228B22", fg="white")
b_start_interface.pack(pady=20, anchor=CENTER)


root.mainloop()
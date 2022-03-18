def redraw_line(event):
    global canvas
    width = event.width
    height = event.height

    coords = canvas.coords("currentline")
    print('Canvas coords:' + str(coords))
    print('Canvas x1:' + str(coords[0]))
    print('Canvas y1:' + str(coords[1]))
    print('Canvas x2:' + str(coords[2]))
    print('Canvas y2:' + str(coords[3]))

def size_changed(event):
    global width_pre, heigth_pre, cnt
    width, heigth = canvas.winfo_width(), canvas.winfo_height()
    cnt = cnt + 1
    if cnt > 1 and (width_pre != width or heigth_pre != heigth):
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
    canvas.bind("<Configure>", redraw_line)

root.bind('<Configure>', size_changed)   # Hook window size changes


# Testing
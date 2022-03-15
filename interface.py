def size_changed(event):
    global width_pre, heigth_pre, cnt
    width, heigth = canvas.winfo_width(), canvas.winfo_height()
    cnt = cnt + 1
    if cnt > 1 and (width_pre != width or heigth_pre!= heigth):
        width_pre, heigth_pre = canvas.winfo_width(), canvas.winfo_height()
        size(event)
    else:
        pass

def size(event):
    global new_image, resized_image
    width, heigth = canvas.winfo_width(), canvas.winfo_height()
    print('Canvas size:', width, 'x', heigth)

    resized_image = palm_img.resize((width, heigth), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    canvas['image'] = new_image
root.bind('<Configure>', size_changed)   # Hook window size changes
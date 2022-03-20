from tkinter import Canvas, Tk, ARC

# Image dimensions
w,h = 640,480

# Create canvas
root = Tk()
canvas = Canvas(root, width = w, height = h, bg = 'white')
canvas.pack()

# curve points
global points_sam
global temp_arc_sam
points_sam = []
temp_arc_sam = None

def arc_sam():
    x_arc_sam = [point_sam[0] for point_sam in points_sam]
    y_arc_sam = [point_sam[1] for point_sam in points_sam]

    return canvas.create_arc(x[0], y[0], x[-1], y[-1], start = 70, style = ARC, width = 8, extent = 90, tags='manualArcSam')

def motion_sam(event):
    global temp_arc_sam
    points_sam.append([event.x, event.y])
    if temp_arc_sam != None:
        canvas_sam.delete(temp_arc_sam)
    temp_arc_sam = arc_sam()


def on_click_release_sam(event):
    arc_sam()
    global points_sam
    points_sam = []

def clear_canvas(event):
    canvas.delete('manualArcSam')

canvas.bind("<B1-Motion>", motion)
canvas.bind("<ButtonRelease-1>", on_click_release)
root.bind("<Key-c>", clear_canvas)

root.mainloop()
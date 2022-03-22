from tkinter import *
from tkinter.font import Font


root = Tk()
root.title('Example 2 fonts')
root.geometry('{}x{}'.format(500, 500))

#Fonts
big_font = Font(family='Helvetica', size=12, weight='bold')
small_font = Font(family='Helvetica', size=8)


container_frame3= Frame(root, highlightbackground="gray80", highlightcolor="gray80", highlightthickness=1,bd=0,bg='red')
container_frame3.grid(row=0,sticky="nsew")
t = Text(container_frame3, font='sans 50 bold')
datalabel= Label(container_frame3, text="{}".format('21.15 %\n\n'),width=12,font=big_font,justify=CENTER,bg='blue')
datalabel.grid(row=0, column=0)
datalabel= Label(container_frame3, text='Mbps', font=small_font)
datalabel.grid(row=0, column=0)


root.mainloop()
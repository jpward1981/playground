from Tkinter import *

index = 0 
def msg():
    global index
    label.configure(text="Testing " + str(index))
    index = index+1
    label.after(1000, msg)

top = Frame()
top.pack()
label=Label(top, text="")
label.configure(text="Testing")
label.pack(side=LEFT, ipadx=50, ipady=50)
top.pack()
label.after(1000, msg)
#top.title("Hello World")
top.mainloop()

import tkinter
from tkinter import *
from os import startfile

root = Tk()
root.title("Swift VPN Installer")

bgimg = tkinter.PhotoImage(file="C:/Users/Kivanc's Account/Downloads/SWIFT VPN.png")
limg = Label(root, i=bgimg)
limg.pack()
def Click():
    title = Label(root, text="Installing Security")
    title.pack()

def Click2():
    path = r""
    startfile(path)

def Click3():
    title = Label(root, text="Running Diagnostic")
    title.pack()

def Click4():
        path = r""
        startfile(path)


# Button
myButton = Button(root, text="Install Security", command=Click)
myButton.pack()

# Button 2
myButton = Button(root, text="Scan Computer", command=Click2)
myButton.pack()

# Button 3
myButton = Button(root, text="Run Diagnostic", command=Click3)
myButton.pack()

# Button 4
myButton = Button(root, text="Customer Support", command=Click4)
myButton.pack()
root.mainloop()

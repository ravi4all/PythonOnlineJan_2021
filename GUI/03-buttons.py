# widgets - textbox, label, button
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("First App")
window.geometry('300x300')

label = Label(window, text = "Hello World", fg='red', bg='white')
label.grid()

def changeText():
    label.configure(text="Bye World")

button = Button(window, text="Click Here", fg='red', command=changeText)
button.grid(column=1, row=0)
# button.grid(column=1, row=1)

window.mainloop()
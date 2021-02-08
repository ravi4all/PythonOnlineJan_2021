# widgets - textbox, label, button
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("First App")
window.geometry('300x300')

# label = Label(window, text = "Hello World", foreground='red', background='black')
# label = Label(window, text = "Hello World", fg='red', bg='black')
label = Label(window, text = "Hello World", fg='red', bg='black',
              width = 20, height = 10)
label.pack()

window.mainloop()
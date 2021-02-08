# widgets - textbox, label, button
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("First App")

label = Label(window, text = "Hello World").pack()
# Label - to display text
# Button - to make clickable buttons
# Entry - single line textbox
# Text  - Multiline text
# Frame - to display a rectangular area to display particular widgets

# pack
# grid
# place

window.mainloop()
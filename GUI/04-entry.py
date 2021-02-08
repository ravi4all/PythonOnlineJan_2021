# widgets - textbox, label, button
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("First App")
window.geometry('300x300')

label_1 = Label(window, text="Greet App", fg='red', bg='white')
label_1.grid(row=0, column=1)

label_2 = Label(window, text="")
label_2.grid(row=1,column=0)

label_3 = Label(window, text="Hello : ", fg='blue')
label_3.grid(row=3,column=0)

# label_4 = Label(window, text="", fg='blue')
# label_4.grid(row=3,column=1)

def greetUser():
    text = text_box.get()
    # label_4.configure(text = text)
    label_3.configure(text=label_3['text'] + " " + text)

text_box = Entry(window, width=20)
text_box.grid(row=2, column=0)

button = Button(window, text="Click Here", fg='red', command=greetUser)
button.grid(column=1, row=2)
# button.grid(column=1, row=1)

window.mainloop()
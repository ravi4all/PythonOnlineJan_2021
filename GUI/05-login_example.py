import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("First App")
window.geometry('600x500')

label_1 = Label(window, text="Login App", fg='red',
                font=('Arial', 20, 'bold'))
label_1.place(x=250, y=30)

label_2 = Label(window, text="Enter your email", fg='red',
                font=('Arial', 16))
label_2.place(x=100, y=130)

text_box_1 = Entry(window, width=20)
text_box_1.place(x=350, y=130)

label_3 = Label(window, text="Enter your password", fg='red',
                font=('Arial', 16))
label_3.place(x=100, y=200)

text_box_2 = Entry(window, width=20)
text_box_2.place(x=350, y=200)

def loginUser():
    useremail = 'ravi@gmail.com'
    userpwd = '1234'
    email = text_box_1.get()
    pwd = text_box_2.get()
    if email == useremail and pwd == userpwd:
        messagebox.showinfo('Success', 'Login Success')
    else:
        messagebox.showinfo('Failure', 'Login Failed')

button = Button(window, text="Click Here",
                fg='red',
                command=loginUser)
button.place(x=250, y=300)

window.mainloop()
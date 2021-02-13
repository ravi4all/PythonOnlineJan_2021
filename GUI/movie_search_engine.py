from tkinter import *
import movie_crawler
from PIL import ImageTk, Image

window = Tk()
window.geometry('1000x500')
window.configure(bg='white')

bg_img = Image.open('img_bg.png')
bg_img = bg_img.resize((1000,500))
bg_render = ImageTk.PhotoImage(bg_img)

label_bg = Label(window, image=bg_render)
label_bg.image = bg_render
label_bg.place(x=0, y=0)

title_label = Label(window, text="Movie Search Engine",
                    fg='blue', font=('Arial',28,'bold'))
title_label.pack()

text_box = Entry(window, width=30,
                 font=('Arial', 20, 'bold'),
                 fg='red')
text_box.place(x=10, y=70)

custom_font = ('Arial', 18, 'bold')

label_1 = Label(window, fg='red',
                font=custom_font)
label_1.place(x=10, y=160)

label_2 = Label(window, fg='red',
                font=custom_font)
label_2.place(x=10, y=260)

label_3 = Label(window, fg='red',
                font=custom_font, wraplength=600)
label_3.place(x=10, y=360)

def show_data():
    movie_name = text_box.get()
    title, rating, summary = movie_crawler.search_movie(movie_name)
    title = "Movie Name : " + title.replace('\n', '')
    rating = "Movie Rating : " + rating.replace('\n', '')
    summary = "Movie Summary : " + summary.replace('\n', '').strip()

    label_1.configure(text=title)
    label_2.configure(text=rating)
    label_3.configure(text=summary)

    img = Image.open('img_1.jpg')
    img = img.resize((200,200))
    render = ImageTk.PhotoImage(img)

    label = Label(window, image=render)
    label.image = render
    label.place(x=500, y=150)


button = Button(window, text="Search Movie", width=20, font=('Arial',15),
                command=show_data)
button.place(x=500, y=66)

window.mainloop()
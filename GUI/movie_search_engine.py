import bs4
import urllib.request as url

from tkinter import *

window = Tk()
window.geometry('1000x500')

title_label = Label(window, text="Movie Search Engine",
                    fg='blue', font=('Arial',28,'bold'))
title_label.pack()

text_box = Entry(window, width=30,
                 font=('Arial', 20, 'bold'),
                 fg='red')
text_box.place(x=10, y=70)

custom_font = ('Arial', 18, 'bold')

label_1 = Label(window, text="Movie Name : ", fg='red',
                font=custom_font)
label_1.place(x=10, y=160)

label_2 = Label(window, text="Movie Rating : ", fg='red',
                font=custom_font)
label_2.place(x=10, y=260)

label_3 = Label(window, text="Movie Summary : ", fg='red',
                font=custom_font, wraplength=600)
label_3.place(x=10, y=360)

def show_data():
    movie_name = text_box.get()
    movie_name = movie_name.replace(' ', '+')
    res = url.urlopen('https://www.imdb.com/find?q={}&ref_=nv_sr_sm'.format(movie_name))
    page = bs4.BeautifulSoup(res, 'lxml')
    td = page.find('td', class_='result_text')
    a_tag = td.find('a')
    href = a_tag.attrs['href']
    path = 'https://www.imdb.com'+href
    res = url.urlopen(path)
    page = bs4.BeautifulSoup(res, 'lxml')
    title = page.find('h1').text
    rating = page.find('div', class_='ratingValue').text
    summary = page.find('div', class_='summary_text').text
    # print(title, page, summary)

    title = label_1['text'] + title.replace('\n', '')
    rating = label_2['text'] + rating.replace('\n', '')
    summary = label_3['text'] + summary.replace('\n', '').strip()

    label_1.configure(text=title)
    label_2.configure(text=rating)
    label_3.configure(text=summary)

button = Button(window, text="Search Movie", width=20, font=('Arial',15),
                command=show_data)
button.place(x=500, y=66)

window.mainloop()
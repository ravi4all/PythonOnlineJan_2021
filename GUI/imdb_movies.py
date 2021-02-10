import bs4
import urllib.request as url

from tkinter import *

res = url.urlopen('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
page = bs4.BeautifulSoup(res, 'lxml')

titles = page.find_all('h3', class_='lister-item-header')
ratings = page.find_all('div', class_='ratings-imdb-rating')
print(len(titles))

window = Tk()
window.geometry('600x500')

movies_list = Listbox(window, width=500, font=('Arial', 15))

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

for i in range(len(titles)):
    movie = titles[i].text.replace('\n', '')
    rating = "Rating : " + ratings[i].text.replace('\n', '')
    movies_list.insert(END, movie)
    movies_list.insert(END, rating)
    movies_list.insert(END, '*' * 100)

movies_list.pack(side=LEFT, fill=BOTH)
scrollbar.config(command = movies_list.yview)

window.mainloop()
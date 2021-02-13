import bs4
import urllib.request as url

def search_movie(movie_name):
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
    img_div = page.find('div', class_='poster')
    img = img_div.find('img')
    img_src = img.attrs['src']
    url.urlretrieve(img_src, 'img_1.jpg')
    return title, rating, summary
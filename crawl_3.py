import bs4
import urllib.request as url

path = 'https://www.freshersworld.com/python-jobs/3535127'
response = url.urlopen(path)
page = bs4.BeautifulSoup(response, 'lxml')

titles = page.find_all('h3', class_='latest-jobs-title')
qualifications = page.find_all('span', class_='qualifications')
desc = page.find_all('span', class_='desc')
for i in range(len(titles)):
    print(titles[i].text.strip())
    print(qualifications[i].text.strip())
    print(desc[i].text.strip())
    print('*' * 20)

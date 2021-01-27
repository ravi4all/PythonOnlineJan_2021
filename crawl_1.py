import bs4
import urllib.request as url

path = 'https://in.indeed.com/java-jobs'
response = url.urlopen(path)
page = bs4.BeautifulSoup(response, 'lxml')

#title = page.find('h2', class_='title')
#print(title.text.strip())

titles = page.find_all('a', class_='jobtitle')
companies = page.find_all('div', attrs={'class':"sjcl"})

for i in range(len(titles)):
    print(titles[i].text.strip())
    print(companies[i].text.strip().replace('\n\n',''))
    print('*' * 20)

import json
import urllib.request as url

name = 'tendulkar'
res = url.urlopen('https://cricapi.com/api/playerFinder?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&name={}'.format(name))

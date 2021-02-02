import urllib.request as url
import json

api_key = '83e01e3dce5d28839bb5a177cb51af12'

path = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format('delhi',api_key)
res = url.urlopen(path)
# print(res)
data = json.load(res)

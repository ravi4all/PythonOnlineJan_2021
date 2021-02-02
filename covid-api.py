import urllib.request as url
import json

path = 'https://api.covid19india.org/states_daily.json'
res = url.urlopen(path)
data = json.load(res)
states = data['states_daily']

confirmed = []
recovered = []
deceased = []

for i in range(len(states)):
    if states[i]['status'] == 'Confirmed':
        confirmed.append(states[i])
    elif states[i]['status'] == 'Recovered':
        recovered.append(states[i])
    else:
        deceased.append(states[i])


# print('Date :', confirmed[0]['date'])
# print('Delhi :', confirmed[0]['dl'])

tail = confirmed[-1:-6:-1]
print("Confirmed cases of last 5 days...")
for i in range(len(tail)):
    print("Date :",tail[i]['date'])
    print("Delhi :",tail[i]['dl'])
    print("Total :",tail[i]['tt'])


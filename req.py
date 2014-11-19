import requests
import json

# # local
# server = 'http://127.0.0.1:8000'
# token = '6d57199da23ffa3603b5213a96ed326f2c5ee39d'

# python anywhere
server = 'http://zymud.pythonanywhere.com:80'
token = '14018c688244c705d9a355d2b9abfd124947e8c9'

# url = server + '/api/signin/'
# r = requests.post(url, {'email': 'admin@i.ua', 'password': 'admin'})
# print r.status_code
# print r.cookies['csrftoken']

headers = {
    'Authorization': 'Token ' + token,
    'Content-Type': 'application/json'
}

##### Current user ######

url = server + '/api/current-user/'
r = requests.get(url, headers=headers)
print r.text


##### Bet subject creation #####

url = server + '/api/bet-subjects/'
data = {
    u'short_description': u'bet short description',
    u'judge': {'email': 'user#8@gmail.com'},
    u'end_datetime': u'2014-11-25T09:29:12.353'
}

r = requests.post(url, data=json.dumps(data), headers=headers)
print r.status_code, r.text

import requests
import sys
import json

base_url = "https://kc.kobotoolbox.org/api/v1/"

data_url = base_url + 'data'
form_url = base_url + 'forms'
user = input("Please enter your username: ")
password = input("Please enter your password: ")
formname = input("Please enter your formname: ")
pk = 0
with requests.Session() as s:
    r = s.get(form_url + '?owner{}'.format(user), auth=(user, password))
    print(r)
    data = json.loads(r.text)
    for i in data:
        # print(i.keys())
        print(('Name: {} formid: {}'.format(i['title'], i['formid'])))
        if i['title'] == formname or i['title'].lower() == formname.lower():
            pk = i['formid']
            print('Found formname: {}, id is: {}'.format(i['title'], i['formid']))
    if pk == 0:
        print('ERROR: formname not found!')
    r.raise_for_status()


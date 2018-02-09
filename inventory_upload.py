import requests
import sys
import json


base_url = "https://kc.kobotoolbox.org/api/v1/"
user = input("Please enter your username: ")
password = input("Please enter your password: ")
formname = input("Please enter your formname: ")
fileloc = input("Please enter the path of the file you want to upload: ")
form_url = base_url + 'forms?owner{}'.format(user)
pk = 0
with requests.Session() as s:
    r = s.get(form_url, auth=(user, password))
    print(r)
    data = json.loads(r.text)
    for i in data:
        print(('Name: {} formid: {}'.format(i['title'], i['formid'])))
        if i['title'] == formname or i['title'].lower() == formname.lower():
            pk = i['formid']
            print('Found: {}, id is: {}'.format(i['title'], i['formid']))
            break;
    if pk == 0:
        print('ERROR: formname not found!')
    upload_url = base_url + 'forms/' + str(pk) + '/csv_import'
    print('url: {}'.format(upload_url))
    files = {'csv_file': open(fileloc, 'rb')}
    r = s.post(upload_url, files=files, auth=(user, password))
    r.raise_for_status()


import requests
import sys
import json


base_url = "https://kc.kobotoolbox.org/api/v1/"

data_url = base_url + 'data/'
user = raw_input("Please enter your username: ")
password = raw_input("Please enter your password: ")
pk = raw_input("Please enter your formid: ")
fileloc = raw_input("Please enter the path of the file you want to upload: ")
form_url = base_url + 'forms/' + pk + '/csv_import'
print(form_url)
with requests.Session() as s:
    r = s.get(form_url, auth=(user, password))
    print(r)
    upload_url = data_url + pk + "/csv_import"
    data = json.loads(r.text)
    for i in data:
        if i == i['title']:
            pk = i['formid']
            print('Name: {} formid: {}'.format(i['title'], i['formid']))
            break
    upload_url = data_url + pk + "/csv_import"
    r = s.get(base_url + 'data?owner{}'.format(user), auth=(user, password))
    print(r)
    print(r.text)
    files = {'csv_file': open('coh-field-upload.csv', 'rb')}
    r = s.post(form_url, files=files, auth=(user, password))
    r.raise_for_status()

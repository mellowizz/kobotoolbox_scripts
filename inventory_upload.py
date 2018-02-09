
import requests
import sys
import json


base_url = "https://kc.kobotoolbox.org/api/v1/"

data_url = base_url + 'data/'
user = input("Please enter your username: ")
password = input("Please enter your password: ")
formname = input("Please enter your formname: ")
# fileloc = input("Please enter the path of the file you want to upload: ")
pk = ''
with requests.Session() as s:
    # r = s.get(base_url, auth=(user, password))
    form_url = base_url + "/forms?owner={}".format(user)
    r = s.get(form_url, auth=(user, password))
    print(r)
    data = json.loads(r.text)
    print('data = {}'.format(data))
    for i, j in enumerate(data):
        print('{}: formname:{} formid: {}'.format(i, j['formtitle'], j['formid']))
        pk = j['formid']
        #print('Found- Name: {} formid: {}'.format(i['title'], i['formid']))
        #break
    if pk == '' or pk is None:
        print("ERROR: PK is null!")
    else:   
        upload_url = data_url + str(pk) + "/csv_import"
        print('url: {}'.format(upload_url))
    '''
    r = s.get(base_url + 'data?owner{}'.format(user), auth=(user, password))
    print(r)
    print(r.text)
    files = {'csv_file': open('coh-field-upload.csv', 'rb')}
    r = s.post(form_url, files=files, auth=(user, password))
    r.raise_for_status()
    '''

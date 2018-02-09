import requests
import sys
import json

base_url = "https://kc.kobotoolbox.org/api/v1/"

data_url = base_url + 'data/' # + pk
user = input("Please enter your username: ")
password = input("Please enter your password: ")
pk = input("Please enter your formid: ")
fileloc = input("Please enter the path of the file you want to upload: ")
form_url = base_url + 'forms/' + pk + '/csv_import'
print(form_url)
with requests.Session() as s:
    r = s.get(form_url, auth=(user, password))
    print(r)
    #r = s.get(base_url + 'data?owner{}'.format(user), auth=(user, password))
    #print(r)
    #print(r.text)
    files = {'csv_file': open(fileloc, 'rb')}
    r = s.post(form_url, files=files, auth=(user, password))
    r.raise_for_status()

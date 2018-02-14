import requests
import sys
import json


base_url = "https://kc.kobotoolbox.org/api/v1/"
post_url = "https://kf.kobotoolbox.org/api/v1/"
# base_url2 = "https://kf.kobotoolbox.org/api/v1/"
user = input("Please enter your username: ")
password = input("Please enter your password: ")
'''name_or_id = input("Type 1 to specify form name and 2 to specify key?\n ")
if name_or_id == 1:
    formname = input("Please enter your formname: ")
    pk = 0
elif name_or_id == 2:
     pk =input("Please enter your formid: ")
else:
    raise("Can't interpret your option")
'''  

formname = input("Please enter your formname: ")
fileloc = input("Please enter the path of the file you want to upload: ")
form_url = base_url + 'forms?owner{}'.format(user)
pk = 0
form_dict = {}
with requests.Session() as s:
    r = s.get(form_url, auth=(user, password))
    print(r)
    data = json.loads(r.text)
    for i in data:
        # print(('Name: {} formid: {}'.format(i['title'], i['formid'])))
        form_dict[i['title']] = i['formid']
        print('Found:\n {}'.format(form_dict))
        if i['title'] == formname or i['title'].lower() == formname.lower():
            pk = i['formid']
            print('Found: {}, id is: {}'.format(i['title'], i['formid']))
            break;
    if pk == 0:
        print('ERROR: formname not found!')

    upload_url = post_url + 'forms/' + str(pk) + '/csv_import'
    print('url: {}'.format(upload_url))
    try:
        files = {'csv_file': open(fileloc, 'rb')}
        r = s.post(upload_url, files=files, auth=(user, password))
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('Encountered an error: {}'.format(e))
    else:
        print("SUCCESS!")

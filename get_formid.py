import requests

dev_token = 'eaf0121bb7d2e85cf71f206b78dfeabdf6068197'
# pk = "150770"

base_url = "https://kc.kobotoolbox.org/api/v1/"

form_url = base_url + 'forms/' + pk + '/csv_import'
data_url = base_url + 'data/' + pk
upload_url = data_url + pk + "/csv_import"
print(upload_url)
with requests.Session() as s:
    r = s.get(base_url, auth=('nmoran', '%C0ll3ctD@t@!'))
    print(r)
    print(r.text)
    r = s.get(base_url + 'data?owner=nmoran', auth=('nmoran', '%C0ll3ctD@t@!'))
    print(r)
    print(r.text)
    files = {'csv_file': open('inventory_tusten.csv', 'rb')}
    r = s.post(form_url, files=files, auth=('nmoran', '%C0ll3ctD@t@!'))
    r.raise_for_status()

import requests
import json
import os
import wx
import gui


class Kobotoolbox(gui.KoboFrame):

    def __init__(self, parent):
        gui.KoboFrame.__init__(self, parent)

    def OnClick(self, e):
        base_url = "https://kc.kobotoolbox.org/api/v1/"
        post_url = "https://kf.kobotoolbox.org/api/v1/"

        user = self.userVal.getValue()
        print("user: {}".format(user))
        password = self.passVal.getValue()
        formname = self.formVal.getValue()
        fileloc = self.csvInventory.getValue()


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

            upload_url = base_url + 'forms/' + str(pk) + '/csv_import'
            print('url: {}'.format(upload_url))
            try:
                files = {'csv_file': open(fileloc, 'rb')}
                r = s.post(upload_url, files=files, auth=(user, password))
                r.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('Encountered an error: {}'.format(e))
            else:
                print("SUCCESS!")

app = wx.App(False)

frame = Kobotoolbox(None)
frame.Show(True)
app.MainLoop()

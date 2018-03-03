#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import sys
from PySide.QtCore import *
from PySide.QtGui import *
import requests
import json

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.username = QLineEdit("username:")
        self.password = QLineEdit("password:")
        self.formname = QLineEdit("formname:")
        self.filebtn = QPushButton("Browse..")
        self.uploadbtn = QPushButton("Upload!")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.formname)
        layout.addWidget(self.filebtn)
        layout.addWidget(self.uploadbtn)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.filebtn.clicked.connect(self.load_file)
        self.uploadbtn.clicked.connect(self.upload)

    # Greets the user
    def upload(self):
        '''
        print ("user: {}".format(self.username.text()))
        print ("password: {}".format(self.password.text()))
        print ("formname: {}".format(self.formname.text()))
        print ("fileloc: {}".format(self.fileloc))
        '''
        base_url = "https://kc.kobotoolbox.org/api/v1/"
        post_url = "https://kf.kobotoolbox.org/api/v1/"
        user = self.username.text()
        password = self.password.text()
        formname = self.formname.text()
        fileloc = self.fileloc

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

    def load_file(self):
        self.fileloc, _ = QFileDialog.getOpenFileName(self, 'Open file')

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())


# always seem to need this
import sys
 
# For PostgreSQL database 
import psycopg2

# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread

# for serial communication
import serial
import time
import threading

# for get data from server using JWT (Json Web Token)
import json
import requests

# This is our window from QtCreator
import mainwindow
import rework

# Variable for getting data from PC Server
dataFactoriesURL = 'http://192.168.10.151:8080/api/factories'
loginURL='http://192.168.10.151:8080/api/auth/login'
headers = {'content-type': 'application/json'}
payload = {
    'email': 'admin@yahoo.com',
    'password': '123qwe'
    }

# Get Token (JWT) using post method
r = requests.post(loginURL,
                  data=json.dumps(payload),
                  headers=headers)
token=r.json()['access_token']
token_type=r.json()['token_type']

# Get data from API using get method and token
hed = {'Authorization':token_type+' '+token}
PARAMS_GET = {'id' : '1'}
r = requests.get(url = dataFactoriesURL, params = PARAMS_GET, headers=hed)
# Convert from single quote mark to double quote mark
json_data=json.dumps(r.json()[0])
# Parsing json data
parsed_json=json.loads(json_data)
# Array of parsed json
id_=str(parsed_json['id'])
email=str(parsed_json['email'])
code=str(parsed_json['code'])
name=str(parsed_json['name'])
phone=str(parsed_json['phone'])

# create class for our Raspberry Pi GUI
class Rework(QMainWindow, rework.Ui_Form):
    def __init__(self):
        global email
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.line_val.setText(name)

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def pb_rework_press(self):
        pass
        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.val_line23.setMargin(20)
        self.val_line24.setMargin(20)
        self.val_line25.setMargin(20)
        self.val_line26.setMargin(20)
        self.pb_rework.released.connect(self.pb_rework_press)
        
# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    mainwin = MainWindow()
    rework = Rework()
    mainwin.show()
    rework.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()

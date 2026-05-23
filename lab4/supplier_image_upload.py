#!/usr/bin/env python3

import os
import requests

url = "http://localhost/upload/"

basedir = os.getcwd() + '/supplier-data/images/'
files = os.listdir(basedir)
for file in files:
  if file.endswith('.jpeg'):
    abspath = os.path.abspath(basedir + '/' + file)
    with open(abspath, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
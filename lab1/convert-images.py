#!/usr/bin/env python3

import os
from PIL import Image

files = os.listdir(os.getcwd()+'/images')
for file in files:
  if not file.startswith('.'):
    abspath = os.path.abspath('images/' + file)
    print(abspath)


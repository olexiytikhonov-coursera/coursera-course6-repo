#!/usr/bin/env python3

import os
from PIL import Image

basedir = os.getcwd() + '/supplier-data/images'
files = os.listdir(basedir)
for file in files:
  if file.endswith('.tiff'):
    abspath = os.path.abspath(basedir + '/' + file)
    img = Image.open(abspath)
    outfile = basedir + '/'+ os.path.splitext(file)[0] + ".jpeg"
    out = img.resize((600,400)).convert("RGB")
    out.save(outfile, "JPEG")
    img.close()




#!/usr/bin/env python3

'lab1 resize and convert images t jpeg'

import os
from PIL import Image

files = os.listdir(os.getcwd()+'/images')
for file in files:
  if not file.startswith('.'):
    abspath = os.path.abspath('images/' + file)
    img = Image.open(abspath)
    outfile = "/opt/icons/" + os.path.splitext(file)[0] + ".jpeg"
#    outfile = os.path.abspath("./images_new/"+os.path.splitext(file)[0] + ".jpeg")
    out = img.rotate(-90).resize((128,128)).convert("RGB")
    out.save(outfile, "JPEG")
    img.close()

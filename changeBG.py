#!/usr/bin/python
#Background Randomizer Script
import shutil
import os
import requests

url = 'https://source.unsplash.com/random/1600x900'
response = requests.get(url, stream=True)
with open('img.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response




os.system("gsettings set org.gnome.desktop.background \
		picture-uri 'file:/home/prdtr/Desktop/Projects/bgRandom/img.jpg'")

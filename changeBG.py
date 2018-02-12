#!/usr/bin/python
#Background Randomizer Script
import shutil
import os,sys
import requests

pathname = os.path.dirname(sys.argv[0])        
curr_dir = os.path.abspath(pathname)



url = 'https://source.unsplash.com/random/1600x900'
response = requests.get(url, stream=True)

f = open('%s/img.jpg'%curr_dir, 'wb')
shutil.copyfileobj(response.raw, f)
del response




os.system("gsettings set org.gnome.desktop.background \
		picture-uri 'file:%s/img.jpg'"%curr_dir)

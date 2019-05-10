#!/usr/bin/env python3

import sys
import time
import logging
from urllib.request import urlopen
import urllib.request
import pandas as pd
import os
import math

from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup

file_name="merged_clean"
data = pd.read_csv(file_name+".csv") 
data=data.dropna(how="all")

os.mkdir(file_name)
os.chdir(file_name)

for index, row in data.iterrows():
	# print(row['Answer.link'])
	if row['Answer.link']!="https://vocaroo.com/" and row['AssignmentStatus']=="Approved" or row['AssignmentStatus']=="Submitted":
	    name=row['Input.song_name']
	    if os.path.exists(name):
	    	os.chdir(name)
	    else:
	    	os.mkdir(name)
	    	os.chdir(name)
	    
	    link=row['Answer.link']
	    idd=link.split("/")[4]
	    d_link="https://s1.vocaroo.com/media/download_temp/Vocaroo_"+idd+".mp3"
	    local_filename, headers = urllib.request.urlretrieve(d_link,filename=(name+"_"+str(index)+".mp3"))
	    os.chdir("..")

#get merged csv
# fileList=["class1.csv","class2.csv","friends.csv","threecents.csv","tencents.csv"]
# output_file = pd.concat([pd.read_csv(filename) for filename in fileList])
# output_file.to_csv("merged.csv", index=False)

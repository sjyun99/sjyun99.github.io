#!/usr/bin/python

import os
import sys
import time
import subprocess

HOUR_LIST = [9, 12, 15, 18, 21]

while True:
    date = subprocess.check_output('date', shell=True)
    date_list = date.replace('  ', ':').replace(' ', ':').split(':')
    hour = int(date_list[3])

    if hour in HOUR_LIST:
        os.system('git add index.html')
        os.system('git commit -m "' + date + '"')
        os.system('git push')
    time.sleep(60*60) # every hour

#!/usr/bin/python

import os
import sys
import time
import subprocess

HOUR_LIST = [6, 12, 18, 21]
INTERVAL = 60*60 # sec

while True:
    date = subprocess.check_output('date', shell=True)
    date_list = date.replace('  ', ':').replace(' ', ':').split(':')
    hour = int(date_list[3])

    if hour in HOUR_LIST:
        t1 = time.time()
        os.system('git add index.html')
        os.system('git commit -m "' + date + '"')
        os.system('git push')
        t2 = time.time()
        tdiff = int(t2 - t1 + 0.5) + 1
        time.sleep(INTERVAL - tdiff) # every hour
    else:
        time.sleep(INTERVAL) # every hour

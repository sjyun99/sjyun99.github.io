#!/bin/bash

DATE=`date`

echo "###" $DATE
git add index.html
git commit -m "$DATE"
git push


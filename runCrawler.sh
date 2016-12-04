#!/bin/bash  
echo "Running crawler"  
sudo pip install -r requirements.txt
cd server
sudo rm dbFile.db
python crawler.py
#!/bin/bash  
sudo server/otherScripts/killServerProcess.sh
echo "Installing dependencies...\n"  
sudo pip install -r requirements.txt
cd server

echo "Running Redis database...\n"
sudo redis-server&

echo "Running crawler...\n"
python crawler.py

echo "Running server...\n"
python server.py

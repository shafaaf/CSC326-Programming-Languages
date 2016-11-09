#!/bin/bash  
echo "Installing dependencies"  
sudo pip install -r requirements.txt
cd server
python server.py

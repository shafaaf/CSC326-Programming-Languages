#!/binu/bash
export DEBIAN_FRONTEND=noninteractive

printf "\nsetupAWS.sh: Running installation script..."

printf "\nsetupAWS.sh: doing apt-get update.."
sudo apt-get update

printf "\nsetupAWS.sh: Installing git.."
sudo apt-get install -y git

printf -ne '\n' | apt-get upgrade -y
sudo apt-get install -y build-essentialnu

printf "\nsetupAWS.sh: Installing python-dev..."
sudo apt-get install -y python-dev

printf "\nsetupAWS.sh: Installing redis-server..."
sudo apt-get install -y redis-server

printf "\nsetupAWS.sh: Installing pip.."
sudo apt-get install -y python-pip

printf "\nInstalling libenchant1c2a..\n"
sudo apt-get install -y libenchant1c2a

printf "\nsetupAWS.sh: Cloning CSC326 project\n"
sudo git clone https://github.com/shafaaf/csc326ProgrammingLanguages.git
sudo chmod -R 777 csc326ProgrammingLanguages/
cd csc326ProgrammingLanguages/

./localSetup.sh

'''printf "\nsetupAWS.sh: Pip installing requirements.txt\n"
sudo pip install -r requirements.txt
cd server

printf "\nsetupAWS.sh: Running redis-server..."
nohup sudo redis-server&

nohup sudo python server.py&
printf "\nsetupAWS.sh: Running python web server..."
'''
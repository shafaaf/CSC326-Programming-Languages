About search engine:
Web application hosted at: http://ec2-54-146-163-48.compute-1.amazonaws.com/
Public DNS: http://ec2-54-146-163-48.compute-1.amazonaws.com/

Important notes:

Initially search engine processing time is slow due to spelling checking for multiple words. Eventually it becomes really fast. 
Each page shows 5 urls. There are links to previous and next pages using buttons. If there are no more URLS to show, the next button will not display anything new. Previous button shows previous URLs that were displayed.
Can test for multiple URLS (more than 5) for example, using search keywords like "computer", "department" etc.

Local machine installation:
The submitted code here is setup to run on a local machine. This will install the required dependencies, run the crawler, run the redis server and start the server.
1. Be at root folder and run the localSetup.sh script as following in the same directory:
	sudo ./localSetup.sh

2. When stopped printing for more than 20 seconds i.e setup complete, then go to url:
	http://localhost:8080


Code Organization (from root folder):
Root folder contains localSetup script, requirements file for pip install and folders for server side, deployment etc,
Deployment scripts are in the deployment folder which includes once click deployment and termination scripts.

Server folder contains the following:
Script folder to automate killing server etc,
Static folder which contains public CSS, Javascript files
Views folder which contains HTML templates for index, results pages etc
Server.py file which handles request routing, spell checking, database query, history table etc
Crawler.py file which contains the crawler that crawls and stores information in a redis-server
Pagerank.py that is used to generate page rankings for links
Getresults.py that uses the redis-server to search for a list of words



Lab 3 benchmarking
RESULT file



AWS instance installation:
All deployment, terminantion, AWS EC2 code is in deployments folder
Note: keys, credentials are not submitted in text form, and key pem file not submitted
To setup the project on a new server in a new instance in AWS:
1. Make a new connection, generate key pairs, and then Run the commands:
cd deployment
sudo python ./oneClickDeployment.py
The public ip and instance id will be printed onto screen and onto a file called deploymentResult.txt. Meanwhile the environment will be setup on the ec2 server.

AWS instance termination:
cd deployment
sudo python ./terminateInstance.py <instanceid>

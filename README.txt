About search engine:
Web application hosted at: http://ec2-54-160-115-230.compute-1.amazonaws.com/
Public DNS: ec2-54-160-115-230.compute-1.amazonaws.com

todo: Benchmarking
c. ab -n 100 -c 16 http://ec2-54-160-115-230.compute-1.amazonaws.com/?keywords=helloworld+foo+bar
see RESULT file

Local machine installation:
The submitted code here is setup to run on a local machine. This assumes that db file generated from crawler is already present. We have already generated and submitted the db file here and so this will work.
To run the project locally (assuming pip installed as TA mentioned):
1. Be at root folder and run the localSetup.sh script as following in the same directory:
	./localSetup.sh
2. Then go to url:
	http://localhost:8080

If want to test crawler, run these commands first: 
1. cd server
2. rm dbFile.db
3. python crawler.py
4. Do as above

AWS installation:
Note: keys, credentials are not submitted in text form
To setup the project on a new server in a new instance in AWS:
1. Make a new connection, generate key pairs, Run the command:
python ./makeInstanceAWSPart1.py
2. Set up the IP address and instance id in makeInstanceAWSPart2.py as seen from online dashboard or print staments from above command
3. (If new instance) Change redirect routes in server.py, index.tpl to the new IP address/redirect
4. python ./makeInstanceAWSPart2.py - This will setup the ubuntu machine with the right dependencies and run the setupAWS.sh script to start the server on that machine

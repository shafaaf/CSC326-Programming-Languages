About search engine:
Web application hosted at: http://ec2-54-160-115-230.compute-1.amazonaws.com/
Public DNS: ec2-54-160-115-230.compute-1.amazonaws.com

Each page shows 5 urls. There are links to previous and next pages using buttons. If there are no more URLS to show, the next button will not display anything new. Previous button shows previous URLs that were displayed.
Can test for multiple URLS (more than 5) for example, using search keywords like "computer", "department" etc.

Important Notes: 
- Some of the URLS are quite long and can take up 2 lines. Therefore for longer ones, please move screen more to the right to see the full URL. 
- Different URLs are separated by an empty line.
- Our search adds a pagerank of 0 for pages that do not have incoming links for which a page rank is not generated in the default implementation Thus, a page rank is added to every page, for pages that don't get automatically generated page ranks, a pagerank of 0 is assigned. This will affect the results of the search engine.



Local machine installation:
The submitted code here is setup to run on a local machine. This assumes that db file generated from crawler is already present. We have already generated and submitted the db file here and so this will work.
To run the project locally (assuming pip installed as TA mentioned):
1. Be at root folder and run the localSetup.sh script as following in the same directory:
	./localSetup.sh
2. Then go to url:
	http://localhost:8080

If want to test crawler ONLY before running search engine, run this command:
1. ./runCrawler.sh

Then can run ../localSetup.sh to run server and go to url.


To run unit tests, follow the commands
1. Go to unitTests
2. Change urls.txt and enter the system dependent path for simple1.html and simple2.html
3. For crawler - python testcrawler.py
4. For persistent storage - python testpersistent.py



Benchmarking
see RESULT file



AWS installation:
Note: keys, credentials are not submitted in text form
To setup the project on a new server in a new instance in AWS:
1. Make a new connection, generate key pairs, Run the command:
python ./makeInstanceAWSPart1.py
2. Set up the IP address and instance id in makeInstanceAWSPart2.py as seen from online dashboard or print staments from above command
3. (If new instance) Change redirect routes in server.py, index.tpl to the new IP address/redirect
4. python ./makeInstanceAWSPart2.py - This will setup the ubuntu machine with the right dependencies and run the setupAWS.sh script to start the server on that machine

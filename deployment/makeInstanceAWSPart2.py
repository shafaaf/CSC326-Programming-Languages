import boto.ec2
import sys
import time
import subprocess

if len(sys.argv) != 3:
	print "incorrect number of arguments passed"
	print "Correct format:\npython terminate.py <instance_id> <public_id>"
	sys.exit()

instance_ID = sys.argv[1]
print 'instance ID is: ', instance_ID

public_ip = sys.argv[2]
print 'public_ip ID is: ', public_ip

try:
	with open ('credentials.csv', 'r') as f:
		lines = f.readlines()
except Exception as exception:
	print "Exception returned: ", exception
	sys.exit()

print "you enteredin instance ID: ", instance_ID

user = 1#int(raw_input("Instance Admin? (Choose number)\n[1] Ismail\n[2] Zen\n[3] Marjan\n--> "))
aws_user_info = lines[user].split(',')
aws_access_key_id = aws_user_info[1].strip()
aws_secret_access_key = aws_user_info[2].strip()

conn = boto.ec2.connect_to_region('us-east-1',
	aws_access_key_id=aws_access_key_id,
	aws_secret_access_key=aws_secret_access_key)


reservations = conn.get_all_reservations()
print "reservations is: ", reservations
'''
instances = reservations[0].instances
print "instances is: ", instances

instances = reservations[1].instances
print "instances is: ", instances
'''


#instances = reservations[2].instances
#print "instances is: ", instances


'''
instances = reservations[3].instances
print "instances is: ", instances

instances = reservations[4].instances
print "instances is: ", instances
'''


# IMP ---Change these as needed. Get from seeing print statements from makeInstanceAWSPart1.py
#myPublicIp = "54.160.115.230"
#myInstanceId = "i-07841355d280673aa"
#key_pair_name = 'key_pair_test2'

myPublicIp = public_ip
myInstanceId = instance_ID
key_pair_name = 'key_pair_test3'


print "Before scp/ssh"
print "ID of instance is: ", myPublicIp
print "IP of instance is: ", myInstanceId

print "Now do the trasfer and run"

#subprocess
#ssh -i key_pair.pem ubuntu@<PUBLIC-IP-ADDRESS>
#scp -i key_pair.pem <FILE-PATH> ubuntu@<PUBLIC-IP-ADDRESS>:~/<REMOTE-PATH>
print "Moving setupAWS.sh to AWS Ubuntu instance at ip address: ", myPublicIp
subprocess.call("scp -i %s.pem -o StrictHostKeyChecking=no setupAWS.sh ubuntu@%s:~/" % (key_pair_name, myPublicIp), shell=True)
print "Moved setupAWS.sh"

print "running script on remote server.."
subprocess.Popen(("ssh -i %s.pem ubuntu@%s /bin/bash ~/setupAWS.sh" % (key_pair_name, myPublicIp)).split())

print "Now setting up environment on ec2"
print "\n\n\nFINAL: Instance ID and Instance IP address: (%s, %s)" % (myInstanceId, myPublicIp)
print "CSC326 Search engine will be running on %s:8080" % myPublicIp
print "Instance ID and public IP returned."




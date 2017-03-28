import boto.ec2
import sys
import time

if len(sys.argv) != 2:
	print "Incorrect number of arguments passed"
	print "Correct format:\npython terminate.py <instance_id>"
	sys.exit()

instance_ID = sys.argv[1]
print 'instance ID is: ', instance_ID

try:
	with open ('credentials.csv', 'r') as f:
		lines = f.readlines()
except Exception as exception:
	print "An exception is returned: ", exception
	sys.exit()

#get parameters
user = 1
aws_user_info = lines[user].split(',')
aws_access_key_id = aws_user_info[1].strip()
aws_secret_access_key = aws_user_info[2].strip()


#connect
conn = boto.ec2.connect_to_region('us-east-1',
	aws_access_key_id=aws_access_key_id,
	aws_secret_access_key=aws_secret_access_key)

instance = conn.terminate_instances(instance_ID.split())

if instance[0].id == instance_ID:
	print "The instance was terminated successfully"
else:
	print "Could not terminate the instance."
	
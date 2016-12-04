

import time
import sys
import subprocess
import os


os.system(pip install -U boto)
import boto.ec2


#-----------------------------------------------------------------------------------------------------------------------

key_pair_name = 'key_pair_test3'

def create():
	print "create:"
	#key_pair_name = 'key_pair'

	'''1. Establish connection to region 'us-east-1' along with aws_access_key_id and aws_secret_access_key'''

	#open the file containing credentials and reads lines
	try:
		with open ('credentials.csv', 'r') as f:
			lines = f.readlines()
	except Exception as exception:
		print "Exception returned: ", exception
		return NULL

	#print lines[1:]

	user = 1#int(raw_input("Instance Admin? (Choose number)
	aws_user_info = lines[user].split(',')
	aws_access_key_id = aws_user_info[1].strip()
	aws_secret_access_key = aws_user_info[2].strip()
	print "aws_user_info: ", aws_user_info
	print "aws_access_key_id: ", aws_access_key_id
	print "aws_secret_access_key: ", aws_secret_access_key

	print "Finished getting aws credentials"

	#boto.ec2.connect_to_region(region_name, **kw_params)
	conn = boto.ec2.connect_to_region('us-east-1', aws_access_key_id=aws_access_key_id, 
		aws_secret_access_key=aws_secret_access_key)
	print "Finished step 1\n"

#-----------------------------------------------------------------------------------------------------------------------

	'''2. Create Key-Pair with boto.ec2.connection.create_key_pair(), which returns a key-pair object, boto.ec2.keypair.KeyPair. 
			The key must be save as a .pem key file using
				boto.ec2.keypair.KeyPair.save(<directory>). The .pem key file is needed for SSH the
					new instances. 
	'''

	try:
		key_pair = conn.create_key_pair(key_pair_name)
		key_pair.save('.')
	except Exception as exception:
		print "Exception returned: ", exception

	print "Finished step 2\n"	

#-----------------------------------------------------------------------------------------------------------------------

	'''3. Create a security group with boto.ec2.connection.create_security_group(), which returns
		an instance of boto.ec2.securitygroup.SecurityGroup. Security group provides restricted
			access only from authorized IP address and ports. For more details, see See
				http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html 
	'''
	


	#Create Security Group
	try:
		security_group = conn.create_security_group('g326','my instance') #return typeboto.ec2.securitygroup.SecurityGroup
	except Exception as exception:
		for i in conn.get_all_security_groups():
			if i.name == 'g326':
				security_group = i
		print "Exception returned: ", exception

	print "security_group is : ", security_group
	

	#print all security groups
	print "printing security groups:"
	for i in conn.get_all_security_groups():
		print i

	print "Finished step 3\n"	

#-----------------------------------------------------------------------------------------------------------------------

	'''
		4. Authorize following protocols and ports for the security group created in step 3:
			4.1. To ping the server, enable
				protocol: ICMP, from port: -1, to port: -1, CIDR IP 0.0.0.0/0
			4.2. To allow SSH, enable
				protocol: TCP, from port: 22, to port: 22, CIDR IP 0.0.0.0/0
			4.3. To allow HTTP, enable
				protocol: TCP, from port: 80, to port: 80, CIDR IP 0.0.0.0/0 
	'''

	print "Trying to authorize"
	try:
		security_group.authorize('ICMP', -1, -1, '0.0.0.0/0')	#ping server
		security_group.authorize('TCP', 22, 22, '0.0.0.0/0')	#allow SSH
		security_group.authorize('TCP', 80, 80, '0.0.0.0/0')	#allow HTTP
		security_group.authorize('TCP', 8080, 8080, '0.0.0.0/0')# for standard port
	except Exception as exception:
		print "Exception returned: ", exception

	#print all permissions
	print "security_group.rules: ",security_group.rules

	print "Finished step 4\n"

#-----------------------------------------------------------------------------------------------------------------------
	'''
		5 and 6. Start a new instance with boto.ec2.connection.run_instance().
			To find Amazon Machine Image (AMI) IDs of Ubuntu server images in various regions,
			please see http://cloud-images.ubuntu.com/releases/14.04.1/release-20140927
			Make sure the property of the selected image matches the instance type and region of
			your selection. For the specification of different EC2 instance types, see
			http://aws.amazon.com/ec2/instance-types. Note that for the purpose of this lab, it is
			sufficient that you use the Micro Instance with the free tier usage.
	'''

	instance_reservation = conn.run_instances(image_id='ami-8caa1ce4', key_name=key_pair_name, 
		security_groups=[security_group.name], instance_type='t1.micro')

	print "boto.ec2.instance.Instance is: ", boto.ec2.instance.Instance

	instance = instance_reservation.instances[0]
	print "instance OR instance_reservation.instances[0] is ", instance
	
	#extra checking
	print "instance.update() is: ", instance.update()
	print "instance.ip_address is: ", instance.ip_address

	print "Finished step 5,6\n"

#-----------------------------------------------------------------------------------------------------------------------

	'''
		7. Once the state of the instance is changed to "running", you can access your instance 
		with the key-pair generated in step 1 with the following command:
				ssh -i key_pair.pem ubuntu@<PUBLIC-IP-ADDRESS>
	'''

	print "Waiting for instance to be ready.."
	while instance.update() != 'running':
		time.sleep(5)

	print "instance.update() is: ", instance.update()
	print "instance.ip_address is: ", instance.ip_address
	#print "boto.ec2.instance.Instance.ip_address is: ", boto.ec2.instance.Instance.ip_address

	print "Instance is now running"
	time.sleep(1)

	#Unsure
	print "Waiting for server to be stable.."
	for i in range(60,0,-1):
		time.sleep(1)
		sys.stdout.write(str(i)+' ')
	sys.stdout.flush()
	print "Server is now stable.."

	print "Instance ID and Instance IP address: %s, %s" % (instance.id, instance.ip_address)
	print "Search engine running on %s on port 8080" % instance.ip_address

#-----------------------------------------------------------------------------------------------------------------------
	print "Now calling part 2 to transfer files."
	variables = "python ./makeInstanceAWSPart2.py " + instance.id + " " + instance.ip_address
	os.system(variables)


if __name__ == '__main__':
	create()	







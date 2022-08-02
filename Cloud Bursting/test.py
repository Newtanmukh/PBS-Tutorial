'''

import subprocess

number=int(input("Please enter the number of PBS Containers which you want to make : "))


# Just for TESTING Purpose, this will simply print hello world into the terminal.
subprocess.call(['echo','Hello World'])


#Getting the HOSTNAME,and storing it in a variable called 'hostname'.
x=subprocess.Popen(['hostname'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
hostname,stderr = x.communicate()
print(hostname)


#Getting the IP Address of the server.
y=subprocess.Popen(['hostname','-I','|','awk','{print $1}'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
ipadd,stderr = y.communicate()
print(ipadd)

'''

import os
import socket
import json
import subprocess
import sys

#The path to the execution package.
#package_path=sys.argv[1]
#print(package_path)

IPaddr=socket.gethostbyname(socket.gethostname())

hostname=socket.gethostname()

number=int(input("Please enter the number of PBS Containers which you want to make : "))

print(IPaddr+' '+hostname)


#Building the docker image
build="docker build -t pbsimage:latest ."
build=str(build)
os.system(build)


add_pbs_source="export PATH=/opt/pbs/bin:$PATH"
os.system(add_pbs_source)

#also,set the flat server uid=1 incase it is disabled by default by the PBS. the flatuid will allow you to submit jobs from the mom containers when you are as a pbsadmin there.
enable_flatuid='qmgr -c"s s flatuid=1"'
os.system(enable_flatuid)


#Creating the number of containers.
for i in range(number):
	command="docker run -td --privileged --name mom{} pbsimage:latest".format(i)    #we should run the moms in privileged mode, since we need to execute commands in it from outside.
	command=str(command)
	os.system(command)



#Updating the /etc/hosts file inside each of the running mom containers.
for i in range(number):
	part1="docker exec -u 0 mom{} /bin/sh -c ".format(i)
	part2="echo '{} {}' >> /etc/hosts".format(IPaddr,hostname)#THIS IS RUNNING FINE.
	start='"'
	end=start
	command=str(part1+start+part2+end)
	os.system(command)

#NOT Needed, since we will be submitting jobs after switching to the pbsadmin user inside the mom container using the command : su - pbsadmin. after that type bash.	
#SO < While you are already inside the as pbsadmin user, you dont need to type source /etc/profile.d/pbs.sh. it will automatically be present since the begining itself.
for i in range(number):
	start='"'
	end=start
	part2="source /etc/profile.d/pbs.sh"
	part1="docker exec -u 0 mom{} /bin/bash -c ".format(i)
	command=str(part1+start+part2+end)
	print(command)
	os.system(command)
	


#Getting the CONTAINER IP Addresses
x=subprocess.Popen(['docker','network','inspect','bridge'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  #Assuming that each container gets created with the default BRIDGE network only.
network_data,stderr = x.communicate()

network_data=str(network_data)


#Converting the data to JSON Format to deal with it in a better way.
json_data = json.loads(network_data)

containers_data=json_data[0]['Containers']

IPs=[]

for x in containers_data.keys():
	IPs.append(containers_data[x]['IPv4Address'])

for i in range(len(IPs)):
	temp=IPs[i].split('/')
	IPs[i]=temp[0]

print(IPs)




#subprocess.call(['source','/etc/profile.d/pbs.sh'])



#Create Node for each of the running PBS COntainers.
for ip in IPs:
	x=str('qmgr -c"c n {}"'.format(ip))
	os.system(x)

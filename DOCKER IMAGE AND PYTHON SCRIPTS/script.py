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

import socket
import json
import subprocess
IPaddr=socket.gethostbyname(socket.gethostname())

hostname=socket.gethostname()

number=int(input("Please enter the number of PBS Containers which you want to make : "))

print(IPaddr+' '+hostname)




#Getting the CONTAINER IP Addresses
x=subprocess.Popen(['docker','network','inspect','bridge'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
network_data,stderr = x.communicate()

network_data=str(network_data)

json_data = json.loads(network_data)

containers_data=json_data[0]['Containers']

IPs=[]

for x in containers_data.keys():
	IPs.append(containers_data[x]['IPv4Address'])

for i in range(len(IPs)):
	temp=IPs[i].split('/')
	IPs[i]=temp[0]

print(IPs)


subprocess.call(['source','/etc/profile.d/pbs.sh'])


#CODE for creating the nodes for each of the Running PBS Containers.



import paramiko
from paramiko_expect import SSHClientInteraction


import time

import re

file = open("output.txt","w+")


 
remote_conn_pre = paramiko.SSHClient()


remote_conn_pre.set_missing_host_key_policy(
	 paramiko.AutoAddPolicy())
hub_ip = {'desired_ip':'Singapore','desired_ip':'United States','desired_ip':'Mumbai'}
# ip = ""
for ip, place in hub_ip.items():

	file.write("\n -----------------------For HUB IP: "+str(ip)+" of " + str(place))
	file.write("\n")
	username= "username" 
	password = "Password"
	remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
	# print ("SSH connection established to %s" % ip)


	remote_conn = remote_conn_pre.invoke_shell()
	# print ("Interactive SSH session established")

	remote_conn.send("\n")
	time.sleep(2)


	remote_conn.send("sat \n")
	time.sleep(2)
	output = remote_conn.recv(5000)
	ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
	output_final = ansi_escape.sub('', output.decode('utf-8'))


	remote_conn.send("sunt\n")
	time.sleep(2)
	output = remote_conn.recv(5000)
	ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
	output_final = ansi_escape.sub('', output.decode('utf-8'))

	remote_conn.send('status cdr-link \n')
	time.sleep(2)
	output = remote_conn.recv(5000)
	
	ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
	output_final = ansi_escape.sub('', output.decode('utf-8'))
	# output_reg = re.sub(r"7F1$",'TESTING',output_final)
	# print ("output is" + output_final + ip)
	output_array = output_final.split('CDR LINK STATUS')
	output_test = output_array[1].split('                             ')
	file.write("\n >>>>>>>>COMMAND: CDR LINK STATUS \n")
	for line in output_test:
		# print (line)
		file.write(str(line)+ "\n \n")

	remote_conn.send("status aesvcs cti-link \n")
	time.sleep(2)
	output = remote_conn.recv(5000)
	ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
	output_final = ansi_escape.sub('', output.decode('utf-8'))
	output_array = output_final.split('\n')
	file.write(">>>>>>>COMMAND: status aesvcs cti-link \n")
	for line in output_array[2:16]:
		# print (line)
		file.write(str(line)+ "\n")
		
	
		
	remote_conn.send("status processor-channels 1 \n")
	time.sleep(2)
	output = remote_conn.recv(5000)
	ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
	output_final = ansi_escape.sub('', output.decode('utf-8'))
	output_final = re.sub('7F1=Cancel F2=Refresh F3=Submit F4=Clr Fld F5=Help F6=Update F7=Nxt Pg F8=Prv Pg 8','\n',output_final)
	output_final = re.sub('7                8Command: ','',output_final)
	output_final = re.sub('Channel Number','\n Channel Number',output_final)
	output_final = re.sub('Session Layer Status','\n Session Layer Status',output_final)
	output_final = re.sub('Socket Status','\n Socket Status',output_final)
	output_final = re.sub('Link Number','\n Link Number',output_final)
	output_final = re.sub('Link Type','\n Link Type',output_final)
	output_final = re.sub('Message Buffer Number','\n Message Buffer Number',output_final)
	output_final = re.sub('Last Failure','\n Last Failure',output_final)
	output_final = re.sub('At','\n At',output_final)
	file.write(">>>>>>>COMMAND: status processor-channels 1 \n")
	
	file.write(str(output_final)+ "\n")
	

	remote_conn.send("status processor-channels 2 \n")
	time.sleep(2)
	output = remote_conn.recv(5000)
	ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
	output_final = ansi_escape.sub('', output.decode('utf-8'))
	output_final = re.sub('7F1=Cancel F2=Refresh F3=Submit F4=Clr Fld F5=Help F6=Update F7=Nxt Pg F8=Prv Pg 8','\n',output_final)
	output_final = re.sub('7                8Command: ','',output_final)
	output_final = re.sub('Channel Number','\n Channel Number',output_final)
	output_final = re.sub('Session Layer Status','\n Session Layer Status',output_final)
	output_final = re.sub('Socket Status','\n Socket Status',output_final)
	output_final = re.sub('Link Number','\n Link Number',output_final)
	output_final = re.sub('Link Type','\n Link Type',output_final)
	output_final = re.sub('Message Buffer Number','\n Message Buffer Number',output_final)
	output_final = re.sub('Last Failure','\n Last Failure',output_final)
	output_final = re.sub('At','\n At',output_final)
	file.write(">>>>>>>COMMAND: status processor-channels 2 \n")	
	
	
	file.write(str(output_final)+ "\n")	

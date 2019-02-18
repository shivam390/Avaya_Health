import paramiko
ssh = paramiko.SSHClient()

#paramiko reject policy and paramiko autoadd policy, which means paramiko rejects the connection host when there is no hostkeys in the known host file auto accept policy automatically accepting the host key and adding them to host file
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

outF = open("output.txt", "w")
hub_ip=('10.190.64.12','10.190.64.17','10.190.68.12','10.190.68.17','10.120.64.12')
for ip in hub_ip:
    outF.write("\n \n------------For IP: "+str(ip))
    outF.write("\n")
    username= "cmorchestra"
    password = "ottawa123"
    ssh.connect(ip, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('df -h')
    output = stdout.readlines()
    for line in output:
        outF.write(line)
        outF.write("\n")
ssh.close()
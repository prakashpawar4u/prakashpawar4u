import paramiko

hostname = "10.10.10.8"
username= "root"
password="root"
log_path = "/data/storage/VILlog/mw/LT4_25jan"
timespan  = 10

print("####"*20)
print("Logging in to  {} as {}".format(hostname, username))
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username = username, password=password)
stdin, stdout, stderr = ssh.exec_command("hostname")
print("Hostname is :",stdout.readlines()[0])

stdin, stdout, stderr = ssh.exec_command("cd {}".format(log_path))

print("Collecting the list of files which are present in the directory {}".format(log_path))
stdin, stdout, stderr = ssh.exec_command("ls -R {}".format(log_path))
output = stdout.readlines()
list_files = []
for i in output:
    list_files.append(i)
print("####"*20)

print("Number of files Present in {} :".format(log_path),len(list_files))
print("####"*20)
stdin, stdout, stderr = ssh.exec_command("find {} -mtime +{} -print".format(log_path,timespan))
#stdin, stdout, stderr = ssh.exec_command("find /data3/SCM_Test/multi_ue_final -mtime +4 | xargs rm -f")


output1 = stdout.readlines()
older_files = []
for j in output1:
    older_files.append(j)
print("Files to be deleted older than {} days: ".format(timespan), len(older_files))


stdin, stdout, stderr = ssh.exec_command("find {} -mtime +{} | xargs rm -f".format(log_path,timespan))

print("####"*20)




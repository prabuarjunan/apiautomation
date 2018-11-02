import paramiko

def ssh_login():
    try:
        mnt = "172.16.55.148:/Prabu-test-volume2"
        sudo = "sudo -s"
        dirname = "pythonscripttest2"
        mkdir = "sudo mkdir" + " " + dirname
        mount = "sudo mount -t nfs -o rw,hard,nointr,rsize=32768,wsize=32768,bg,nfsvers=3,tcp" + " " + mnt + " " + dirname
        hostname1 = "ec2-34-201-249-13.compute-1.amazonaws.com"
        cert = paramiko.RSAKey.from_private_key_file("/Users/arjunan/Documents/prabu.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print ("connecting...")
        c.connect( hostname = hostname1, username = "ec2-user", pkey = cert )
        print("connected!!!")
        stdin, stdout, stderr = c.exec_command(mkdir)
        stdin1, stdout1, stderr1 = c.exec_command(mount)
        print(stdout.readlines())
        print(stdout1.readlines())
        c.close()

    except:
        print("Connection Failed!!!")


ssh_login()
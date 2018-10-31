import boto3
import time
import paramiko

# initialize cft and ec2

cft = boto3.client('cloudformation')
ec2 = boto3.client('ec2')

# create stack

def  createStack():
    stackname = "prabuTest9"
    with open('//users/arjunan/Documents/EC2instnaceSample.json', 'r') as f:
        create_cft = cft.create_stack(StackName=stackname, TemplateBody=f.read())
    print("Create Stack o/p - ", create_cft)

# wait time for the Stack creation

    time.sleep(20)

# list the stack created

    list_stack_resp = cft.list_stack_resources(StackName=stackname)
    instanceID = list_stack_resp['StackResourceSummaries'][0]['PhysicalResourceId']
    print(instanceID)

def mount(machinename, username, dirname, filename, data):
    ip='server ip'
    hostname = 'hostname'
    port = 22
    username = 'username'
    password = 'password'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    print(resp)

    stdin, stdout, stderr = ssh.exec_command('some really useful command')
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    print(resp)

    # sftp = ssh.open_sftp()
    # try:
    #     sftp.mkdir(dirname)
    # except IOError:
    #     pass
    # f = sftp.open(dirname + '/' + filename, 'w')
    # f.write(data)
    # f.close()
    # ssh.close()


data = 'This is arbitrary data\n'.encode('ascii')
put_file('v13', 'rob', '/tmp/dir', 'file.bin', data)


createStack()
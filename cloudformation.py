import boto3
import time
import paramiko
from class_getRequest import cvsAPI

cvs = cvsAPI()
cvs.get_fileSystems()
cvs.get_fileSystemsdetails()
cvs.create_fileSystems()
#update_fileSystems()
#delete_filesystems()
#cvs.create_snapshot()
cvs.target_information()
mnt = cvs.buildMountnameforCFT()
print(mnt)

cft = boto3.client('cloudformation')

class cftStack():

    # create stack

    def createStack(self):
        stackname = "prabuTest36"
        with open('//users/arjunan/Documents/EC2instnaceSample.json', 'r') as f:
            create_cft = cft.create_stack(StackName=stackname, TemplateBody=f.read())
        print("Create Stack o/p - ", create_cft)

    # wait time for the Stack creation

        time.sleep(120)

    # list the stack created

        list_stack_resp = cft.list_stack_resources(StackName=stackname)
        if list_stack_resp['StackResourceSummaries'][0] != 0:
            instanceID = list_stack_resp['StackResourceSummaries'][0]['PhysicalResourceId']
            self.instanceID = instanceID
            print(instanceID)
        else:
            print("Stack Creation failed")

    #get the public DNS of the Intance created

    def intanceDetails(self):
        requiredInstance = self.instanceID
        print(requiredInstance)
        ec2client = boto3.client('ec2')
        response = ec2client.describe_instances()
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                # This sample print will output entire Dictionary object
                print(instance)
                # This will print will output the value of the Dictionary key 'InstanceId'
                print(instance["InstanceId"])
                if (instance["InstanceId"]) == requiredInstance:
                    response = ec2client.describe_instances(
                        Filters=[
                            {
                                'Name': 'instance-id',
                                'Values': [requiredInstance]
                            },
                        ])
                    publicipAddress = response['Reservations'][0]['Instances'][0]['PublicDnsName']
                    self.publicipAddress = publicipAddress
                    print("publicipAddress", publicipAddress)
                else:
                    print("Instance not Found")



    def ssh_login(self):

        try:
            export = mnt
            sudo = "sudo -s"
            dirname = "pythonscripttest4"
            mkdir = "sudo mkdir" + " " + dirname
            mount = "sudo mount -t nfs -o rw,hard,nointr,rsize=32768,wsize=32768,bg,nfsvers=3,tcp" + " " + export + " " + dirname
            hostname1 = self.publicipAddress
            cert = paramiko.RSAKey.from_private_key_file("/Users/arjunan/Documents/prabu.pem")
            c = paramiko.SSHClient()
            c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print ("connecting...")
            time.sleep(120)
            #c.connect(hostname="ec2-54-88-57-117.compute-1.amazonaws.com", username="ec2-user", pkey=cert)
            c.connect(hostname=hostname1, username="ec2-user", pkey=cert)
            print("connected!!!")
            stdin, stdout, stderr = c.exec_command(mkdir)
            stdin1, stdout1, stderr1 = c.exec_command(mount)
            print(stdout.readlines())
            print(stdout1.readlines())
            c.close()

        except:
            print("Connection Failed!!!")

stack = cftStack()
stack.createStack()
stack.intanceDetails()
stack.ssh_login()


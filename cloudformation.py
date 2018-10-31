import boto3
import time
from getRequest import target_information

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

createStack()



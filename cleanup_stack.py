import boto3

stack_session = boto3.client('cloudformation')

class cleanupStack(object):
    def listStack(self):
        stacks = stack_session.get_paginator('list_stacks')
        response_iterator = stacks.paginate(StackStatusFilter=['CREATE_COMPLETE'])
        for page in response_iterator:
            stack = page['StackSummaries']
            for i in stack:
                print(i)
                if i['StackName'] == "IAAS":
                    stack_session.delete_stack(StackName=i['StackName'])
                    print("deleted")

                else:
                    print("No Match stack found")
                print(['StackName'])


cleanupinfo = cleanupStack()
cleanupinfo.listStack()
#cleanupinfo.deleteStack()





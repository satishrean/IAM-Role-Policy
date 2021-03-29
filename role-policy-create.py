import json
import boto3
import botocore
import argparse
import glob
import re
import os
import getopt
import sys
from botocore.exceptions import ClientError
parser = argparse.ArgumentParser(description="This Module is to create iam role and policy")
parser.add_argument("-p", "--policy", required=True)
parser.add_argument("-r", "--role", required=True)
args = parser.parse_args()
policy = args.policy
role = args.role
argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'p:r:')
l = []
for opt, arg in opts:
    if opt in ['-p']:
        policy_name = arg
        #print(policy_name)
        for ppart in policy_name.split(","):
            print(ppart)
            try:
                f = open(ppart+'.json', 'r')
                pvalue = f.read()
                #print(pvalue)
                policy_document = json.loads(json.dumps(pvalue))
                #print(assume_policy_document)
                client = boto3.client('iam')
                create_policy_response = client.create_policy(
                    PolicyName = ppart,
                    PolicyDocument = policy_document
                )
                #print(create_policy_response)
            except ClientError as error:
                if error.response['Error']['Code'] == 'EntityAlreadyExists':
                    print('Policy already exists... hence exiting from here')
                else:
                    print('Unexpected error occurred... Policy could not be created', error)
            iam = boto3.client('iam')
            response = iam.list_policies(
                Scope = 'All' # 'AWS'|'Local'|'All'
            )
            for each_policy in response['Policies']:
                if(each_policy['PolicyName'] == ppart):
                    #print(each_policy['PolicyName'])
                    #print(each_policy['Arn'])
                    arn = each_policy['Arn']
                    l.append(arn)
        #print(l)
    elif opt in ['-r']:
        role_name = arg
        #print(role_name)
        i = 0
        for rpart in role_name.split(","):
            print(rpart)
            try:
                f = open(rpart+'.json', 'r')
                rvalue = f.read()
                #print(rvalue)
                assume_role_document = json.loads(json.dumps(rvalue))
                #print(assume_role_document)
                client = boto3.client('iam')
                create_role_response = client.create_role(
                    RoleName = rpart,
                    AssumeRolePolicyDocument = assume_role_document
                )

                attach_response = client.attach_role_policy(
                    RoleName=rpart, PolicyArn=l[i])
                i = i + 1
            except ClientError as error:
                if error.response['Error']['Code'] == 'EntityAlreadyExists':
                    print('Role already exists... hence exiting from here')
                else:
                    print('Unexpected error occurred... Role could not be created', error)

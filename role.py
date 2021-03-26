import boto3

client = boto3.client('sts')
service_client = boto3.client(
        resource_type, region_name=region,
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken']
        )
return service_client

role_name = "assume_role"

aws_con=boto3.session.Session(profile_name="default")

iam_list=aws_con.resource('iam')

for each_role in iam_list.roles.all():
    if(each_role.name == role_name):
        print(each_role.name);

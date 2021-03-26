import boto3

role_name = "assume_role"

aws_con=boto3.session.Session(profile_name="default")

iam_list=aws_con.resource('iam')

for each_role in iam_list.roles.all():
    if(each_role.name == role_name):
        print(each_role.name);

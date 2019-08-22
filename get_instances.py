# A simple python script to list all the running EC2 instances in AWS and its state
import boto3
session=boto3.session.Session(profile_name="dev_root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-1")
for each_in in ec2_con_re.instances.all():
    print (each_in.id,each_in.state)

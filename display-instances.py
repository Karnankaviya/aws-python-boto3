import boto3
import pprint
# Get the AWS console login
session = boto3.session.Session(profile_name="capgemini_prod")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=session.client(service_name="ec2",region_name="us-east-1")
#pprint.pprint(ec2_con_cli.describe_instances()["Reservations"])  
for each_info in (ec2_con_cli.describe_instances()["Reservations"]):
    for instanceinfo in ((each_info["Instances"])):
        print(instanceinfo["InstanceId"],instanceinfo["InstanceType"])
        
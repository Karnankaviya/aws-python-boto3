#Import boto3 for python operations within AWS
import boto3
#Login into AWS console using dev_root account
session=boto3.session.Session(profile_name="capgemini_prod")
#Get into the EC2 page
ec2_console_resource=session.resource(service_name="ec2",region_name="us-east-1")
#print dir(ec2_console_resource)
#Get the input of the instance number from the user to find its status
instance_id=input("Enter your instance id to the status: ")
# To find the status of the instance
my_instance=ec2_console_resource.Instance(id=instance_id)
#Print the status os the instance
print (my_instance.state['Name'])
import boto3
# The below is used to establish session with AWS EC2 console
session=boto3.session.Session(profile_name="EC2_S3_IAM")
# The below is used to contact AWS resource
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
# The below is used to contact AWS client
ec2_con_cli=session.resource(service_name="ec2",region_name="us-east-2")

#S3 console
s3_con_re = session.resource(service_name="s3",region_name="us-east-1")
s3_con_cli=session.resource(service_name="s3",region_name="us-east-2")
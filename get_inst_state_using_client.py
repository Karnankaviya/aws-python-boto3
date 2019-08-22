import boto3
# Get the AWS console login
session = boto3.session.Session(profile_name="capgemini_prod")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-1")
instance_id = "i-0fe7a8dc12230b9e7"
#Creating instance object
my_instance=ec2_con_re.Instance(id=instance_id)
while True:

    print("1. Start your instance")
    print("2. Stop your instance")
    print("3. Restart your instance")
    print("4. Terminate your instance")
    print("5 Exit")
    choice = int(input("Please select one of the choice : "))
    if choice ==1:
        my_instance.start()
        my_instance.wait_until_running()
        print("Your instance is now STARTED {}".format(instance_id))
    elif choice==2:
        my_instance.stop()
        my_instance.wait_until_stopped
        print("Your instance is now STOPPED {}".format(instance_id))
    elif choice==3:
        my_instance.reboot()
        my_instance.wait_until_running()
        print("Your instance is now REBOOTED {}".format(instance_id))
    elif choice ==4:
        my_instance.terminate()
        my_instance.wait_until_terminated()
        print("Your instance is now TERMINATED {}".format(instance_id))
    elif choice ==5:
        print("See you next time")
        break
    else:
        print("Please provide a valid input")
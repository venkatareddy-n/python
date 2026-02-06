import boto3

# AWS region and EC2 instance IDs (replace with your values)
region = 'us-east-1'
instance_ids = ['i-0123456789abcdef0']  # Add one or more instance IDs

ec2 = boto3.client('ec2', region_name=region)

def start_instances():
    response = ec2.start_instances(InstanceIds=instance_ids)
    print("Starting instances:", instance_ids)
    print(response)

def stop_instances():
    response = ec2.stop_instances(InstanceIds=instance_ids)
    print("Stopping instances:", instance_ids)
    print(response)

# Example usage
if __name__ == "__main__":
    action = input("Enter 'start' to start or 'stop' to stop the instances: ").strip().lower()
    if action == "start":
        start_instances()
    elif action == "stop":
        stop_instances()
    else:
        print("Invalid action. Please enter 'start' or 'stop'.")

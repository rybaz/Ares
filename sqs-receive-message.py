import boto3
import os
import requests

sqs = boto3.client('sqs')
s3 = boto3.resource('s3')
sns = boto3.client('sns')
ec2 = boto3.client('ec2')

r = requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document")
response_json = r.json()
region = response_json.get('region')
instance_id = response_json.get('instanceId')

queue_url = '<SQS_QUEUE_URL>'

# send succesfull launch message
snsNotification = sns.publish(
    # TODO: Change Static Names to ENVariables
    TopicArn='<SNS_TOPIC_ARN>',
    Message='Ares Instance Launched Successfully'
)

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']
attrs = message['MessageAttributes']

os.system("sudo hashcat -m 0 -a 0 " + attrs['Hash']['StringValue'] + " /home/ubuntu/cracking/wordlists/rockstation.txt -o /home/ubuntu/results.txt")

print("os system is done")

# upload completed file to s3
s3.meta.client.upload_file('/home/ubuntu/results.txt', 'ares-hash-dump', 'results.txt')

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)

print('Received and deleted message: %s' % message)

# Push SNS Notification

snsNotification = sns.publish(
    # TODO: Change Static Names to ENVariables
    TopicArn='<SNS_TOPIC_ARN>',
    Message='Hashcat Executed Successfully'
)

# terminate instance

ec2_terminate = ec2.terminate_instances(
    InstanceIds=[
        instance_id
    ],
    DryRun=False
)

import boto3
import os

sqs = boto3.client('sqs')
s3 = boto3.resource('s3')
sns = boto3.client('sns')

queue_url = 'https://sqs.us-east-1.amazonaws.com/175722996601/ares-hash-queue'

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
attrs = message['MessageAttributes']

os.system("sudo hashcat -m 0 -a 0 " + attrs['Hash']['StringValue'] + " /home/ubuntu/cracking/wordlists/rockstation.txt -o /home/ubuntu/results.txt")

# choose message to receive
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
    TopicArn='arn:aws:sns:us-east-1:175722996601:ares-setup-cft-SNSTopic-AFEZ96WT3RZZ',
    Message='Hashcat Executed Successfully'
)
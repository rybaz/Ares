import boto3

sqs = boto3.client('sqs')

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

print("sudo hashcat -m 0 -a 0 " + attrs['Hash']['StringValue'] + " /home/ubuntu/cracking/wordlists/rockstation.txt")

# choose message to receive

# delete message
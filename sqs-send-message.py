import boto3
import time

sqs = boto3.resource('sqs')
s3 = boto3.resource('s3')

queue = sqs.get_queue_by_name(QueueName='ares-hash-queue')
queue_url = "https://sqs.us-east-1.amazonaws.com/175722996601/ares-hash-queue"
MessageAttrList = ["Hash"]
MessageAttr = {}

def sendMessage(MessageAttributes):
    try:
        response = queue.send_message(
            MessageBody = "A Give Hash",
            MessageAttributes = MessageAttributes)

        http_code = response['ResponseMetadata']['HTTPStatusCode']

        if (http_code == 200):
            print("success!")
        else:
            print("message failed")

    except:
        print("Message Failed to send....")

# body = input("Create the message body: ")

for attr in MessageAttrList:
    # attributeType = input("Insert your Attribute Type: ")
    attributeTypeValue = input("Insert the corresponding value for " + attr + ": ")
    MessageAttr[attr] = {
        'StringValue' : attributeTypeValue,
        'DataType' : 'String'
    }

print(MessageAttr)

sendMessage(MessageAttr)

# Catch Crached Password from S3

while(True):
    try:
        # TODO: change static names to ENVariables
        s3.meta.client.download_file('ares-hash-dump', 'results.txt', '/home/stefantjie/Ares/results.txt')
        print("success")
        break
    except:
        print("waiting...")
        time.sleep(15)
        continue
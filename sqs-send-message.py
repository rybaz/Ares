import boto3
import time
import os

sqs = boto3.resource('sqs')
s3 = boto3.resource('s3')

queue = sqs.get_queue_by_name(QueueName='ares-hash-queue')
queue_url = "https://sqs.us-east-1.amazonaws.com/175722996601/ares-hash-queue"
MessageAttrList = ["Hash"]
MessageAttr = {}

def sendMessage(MessageAttributes):
    try:
        response = queue.send_message(
            MessageBody = "A Given Hash",
            MessageAttributes = MessageAttributes)

        http_code = response['ResponseMetadata']['HTTPStatusCode']

        if (http_code == 200):
            print("Successfully sent hash for cracking!")
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

print("Creating EC2 instance....")

#os.system("bash spot-request-command.sh")

#print("Instance created successfully...")
time.sleep(5)
# Catch Cracked Password from S3

while(True):
    try:
        # TODO: change static names to ENVariables                    vvvvv makes this your directory
        s3.meta.client.download_file('ares-hash-dump', 'results.txt', '/Users/stefanbekker/Documents/Programming/Ares/results.txt')
        print("Hash cracked! Plaintext saved to results.txt in " + os.getcwd())
        break
    except:
        print("Waiting on Hashcat to finish...")
        time.sleep(15)
        continue
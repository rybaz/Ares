import boto3

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='ares-hash-queue')
queue_url = "https://sqs.us-east-1.amazonaws.com/175722996601/ares-hash-queue"
MessageAttrList = ["HashType","Mask"]
MessageAttr = {}

def sendMessage(body, MessageAttributes):
    try:
        response = queue.send_message(
            MessageBody = body,
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

"""
while (True):
    attributeType = input("Insert your Attribute Type: ")
    attributeTypeValue = input("Insert the corresponding value: ")
    MessageAttr[attributeType] = {
        'StringValue' : attributeTypeValue,
        'DataType' : 'String'
    }

    answer = input("Would you like to add more attributes? Y/N: ")

    if (answer == "N" or answer == "n"):
        break
"""
print(MessageAttr)

sendMessage("body", MessageAttr)
import boto3

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='my-dev-queue')
queue_url = "https://queue.amazonaws.com/456336145658/my-dev-queue"
MessageAttr = {}

def sendMessage(body, MessageAttributes):
    '''
    body = input("Insert body: ")
    value1 = input("Insert val1: ")
    value2 = input("Insert val2: ")
    value3 = input("Insert val3: ")
    ''' 
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

body = input("Create the message body: ")

while (True):
    attributeType = input("Insert your Attribute Type: ")
    attributeTypeValue = input("Insert the corresponding value: ")
    MessageAttr[attributeType] = {
        'StringValue' : attributeTypeValue,
        'DataType' : 'String'
    }

    answer = input("Would you like to add more attributes? Y/N: ")

    if (answer == "N"):
        break

print(MessageAttr)

sendMessage(body, MessageAttr)
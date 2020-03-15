import boto3

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName="my-dev-queue")

# establish queue
"""
def select_queue():
    # queue iterator
    for i in sqs.queues.all():
        print(i.url)
    # set queue to user specified
    user_selected_queue = input("Which queue would you like? ")
    global queue 
    queue = sqs.get_queue_by_name(QueueName=user_selected_queue)

select_queue()
"""
# Iterate accross messages in choosen queue

for message in queue.receive_messages(MessageAttributeNames=['All']):
    print(message)
"""
# Process messages by printing out body and optional author name
for message in queue.receive_messages(MessageAttributeNames=['HashType']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('HashType').get('StringValue')
        if author_name:
            author_text = ' ({0})'.format(author_name)

    # Print out the body and author (if set)
    print('Hello, {0}!{1}'.format(message.body, author_text))
    
    message.delete()
    """
# choose message to receive

# delete message
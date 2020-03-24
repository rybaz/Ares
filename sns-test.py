import boto3

sns = boto3.client('sns')

snsNotification = sns.publish(
    # TODO: Change Static Names to ENVariables
    TopicArn='arn:aws:sns:us-east-1:175722996601:ares-setup-cft-SNSTopic-AFEZ96WT3RZZ',
    Message='Suppies'
)
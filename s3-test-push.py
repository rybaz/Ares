import boto3
import time

s3 = boto3.resource('s3')

s3.meta.client.upload_file('/home/stefantjie/Ares/rockstation.txt', 'ares-hash-dump', 'rockstation.txt')

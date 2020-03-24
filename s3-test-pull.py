import boto3
import time

s3 = boto3.resource('s3')

while(True):
    try:
        s3.meta.client.download_file('ares-hash-dump', 'rockstation.txt', '/home/stefantjie/Ares/rockstation-2.txt')
        print("success")
        break
    except:
        print("waiting...")
        time.sleep(15)
        continue
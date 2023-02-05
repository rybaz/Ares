#!/bin/sh

# POST AMI LAUNCH

## Set up Nvidia driver and test kernal module load for OpenCL
# sudo /bin/bash /home/ubuntu/cracking/drivers/NVIDIA-Linux-x86_64-410.72.run --ui=none --no-questions --silent -X && sudo nvidia-smi

## Run receive script
python3 /home/ubuntu/sqs-receive-message.py &

echo 'Script completed'

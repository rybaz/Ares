<p align="center">
  <img width="400" height="318" src="https://www.storynory.com/wp-content/uploads/2017/02/xares-450.jpg.pagespeed.ic.1bEsYlQq-6.jpg">
</p>

# Ares
High-impact, high-efficiency password cracking using GPUs in AWS. The best part? It's open-source.

## What does it do?
The goal of this project was to create and easy and cost-efficient way to crack passwords using
GPU-heavy EC2 instances. By using spot instances and Lambda/CDK, we can run all of this from
a Python script.

## Prerequisites
1. An AWS account
2. Permission from AWS to use p3 instances
3. A connected payment method
4. Our custom AMI

## Associated Projects
* masker.py

## Necessary installations and configurations
## OS
`sudo apt-get update && sudo apt-get install hashcat make gcc wget`

## Nvidia drivers:
`sudo /bin/bash /home/ubuntu/cracking/drivers/NVIDIA-Linux-x86_64-410.72.run --ui=none --no-questions --silent -X && sudo nvidia-smi`

## Run receive script for cron at boot
`@reboot python3 /home/ubuntu/sqs-receive-message.py &`

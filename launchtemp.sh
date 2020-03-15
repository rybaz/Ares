#!/bin/sh
sudo apt-get update && sudo apt-get install hashcat wget 

# Download and install Tesla drivers
wget http://us.download.nvidia.com/tesla/410.72/NVIDIA-Linux-x86_64-410.72.run
sudo /bin/bash NVIDIA-Linux-x86_64-410.72.run --ui=none --no-questions --silent -X

# Verify that drivers installed correctly
sudo nvidia-smi

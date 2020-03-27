#!/bin/bash
aws ec2 request-spot-instances --spot-price "15" --instance-count 1 --type "one-time" --block-duration-minutes 60 --launch-specification file://specification.json
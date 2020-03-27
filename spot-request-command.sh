#!/bin/bash
aws ec2 request-spot-instances --spot-price "7.5" --launch-specification file://specification.json
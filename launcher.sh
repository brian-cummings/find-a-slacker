#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python scrip$

cd /
cd home/pi/python/find-a-slacker
# Wait for network to be up (pinging Google)
while ! ping -c 1 -W 1 8.8.8.8; do
    sleep 1
done
python startup.py
python sensor.py

#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python scrip$

cd /
cd home/pi/python/slacker
{ python startup.py; } &
python sensor.py



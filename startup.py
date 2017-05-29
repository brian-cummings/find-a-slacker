import netifaces as ni

import caller

ni.ifaddresses('en0')
ip = ni.ifaddresses('en0')[2][0]['addr']
print ip  # should print "192.168.100.37"
caller.slack_ip(ip)
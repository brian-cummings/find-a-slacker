import netifaces as ni
import caller

ip = ni.ifaddresses('wlan0')[2][0]['addr']
print ip  # should print "192.168.100.37"
caller.slack_ip(ip)
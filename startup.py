import netifaces as ni
import caller

ip = ni.ifaddresses('wlan0')[2][0]['addr']
caller.slack_ip(ip)
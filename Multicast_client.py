#!/usr/bin/env python
#coding=utf-8

import time
import struct
from socket import *
import sys


if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    MYPORT = 8080   #发送数据到该端口

if sys.argv[2:]:
    MYGROUP = str(sys.argv[2])
else:
    MYGROUP = '224.1.2.3'  # 组播组

	
SENDERIP = '192.168.2.194'#本地ip
SENDERPORT = 1501#本地接口

MYTTL = 255 # 发送数据的TTL值
 
 

def sender():
    s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)
    s.bind((SENDERIP,SENDERPORT))
    # Set Time-to-live (optional)
    ttl_bin = struct.pack('@i', MYTTL)
    s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl_bin)
    status = s.setsockopt(IPPROTO_IP,
        IP_ADD_MEMBERSHIP,
        inet_aton(MYGROUP) + inet_aton(SENDERIP))#加入到组播组
    while True:
        data = 'data_001'
        s.sendto(data + '\0', (MYGROUP, MYPORT))
        print "send data ok !"
        time.sleep(10)
 
if __name__ == "__main__":
    sender()

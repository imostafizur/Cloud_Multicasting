#!/usr/bin/env python
#coding=utf-8

import time
import socket
import sys

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8888

if sys.argv[2:]:
    host = str(sys.argv[2])
else:
    host = '127.0.0.1'


local_addr = (host,port)
buff_len = 1024

if __name__ == '__main__':

    # 创建一个socket
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定监听的地址和端口
    udp.bind(local_addr)
    
    while True:

        print('wating for message...')
        # 阻塞接收客户端数据
        data, addr = udp.recvfrom(buff_len)
        print('received from %s data:%s' % (addr, data.decode('utf-8')))

        time.sleep(1.5)
        # 发送数据给客户端
        udp.sendto(('server '+str(time.time())).encode('utf-8'), addr)

    # 关闭socket  
    udp.close()

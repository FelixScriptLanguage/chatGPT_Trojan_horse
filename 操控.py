# -*- coding: utf-8 -*-
import os

import socket
import threading
import time
rd = open('./config/lj.txt','r',encoding='utf-8').read().split(',')
ip = rd[0]
port = int(rd[1])
ip_port = (ip,port)

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(ip_port)

def js():
    while True:
        date=sk.recv(8192)#接受信息
        content = date.decode('utf-8')
        if content[:5] == 'king:':
            continue
        else:
            print(date.decode('utf-8'))

sw=threading.Thread(target=js)
sw.setDaemon(1)
sw.start()
while True:
    time.sleep(0.5)
    date=input();dt = 'king:'+date
    if date == 'clear':
        os.system('cls')
        continue
    else:
        sk.send(dt.encode(encoding='utf-8'))
sk.close#结束连接

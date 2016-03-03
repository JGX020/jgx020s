#!/usr/bin/python
from socket import *
import os.path
import sys
ipstr=open('ippool.txt').read()
ips=ipstr.split(',')
def get_header (name):
        leng = len(name)
        assert leng < 250
        return chr(leng) + name

def send_file (name,ip):
        basename = os.path.basename(name)
        header = get_header(basename)
        cont = open(name).read()
        s = socket (AF_INET, SOCK_STREAM)
        s.connect((ip,1234))
        s.sendall (header)
        s.sendall (cont)
        s.close()

if __name__=='__main__':
        for ip in ips:
            send_file ('5.txt',ip)

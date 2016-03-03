#!/usr/bin/python
import SocketServer
import database
import client
# Format: name_len      --- one byte
#         name          --- name_len bytes
#         data          --- variable length
# Save data to name into current directory
addr = ('120.55.82.93', 1234)

ipstr=open('ippool.txt').read()
ips=ipstr.split(',')
class MyTCPHandler (SocketServer.StreamRequestHandler):
        def handle (self):
                name_len = ord(self.rfile.read(1))
                name = self.rfile.read(name_len)
                print "Get request:%s"%name
                fd = open(name, 'w')
                fa = open('tmp.txt','w')
                cont = self.rfile.read(4096)    
                while cont:
                        fd.write(cont)
                        cont = self.rfile.read(4096)
                if database.seldatabase('users') is None:
                        fa.write('true')
                fa.close()
                for ip in ips:
                    client.send_file ('tmp.txt',ip)
                fd.close()
                print "Out :%s"%name


if __name__=='__main__':
           server = SocketServer.TCPServer(addr, MyTCPHandler)
           server.serve_forever()

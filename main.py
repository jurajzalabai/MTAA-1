
# proxy code from: https://github.com/tirfil/PySipFullProxy

# from proxy import UDPHandler
import socketserver
import proxy



if __name__ == '__main__':
    #ipadress = input()
    #PORT = int(input())
    #HOST = input()
    ipaddress = "147.175.163.113"
    PORT = 5060
    HOST = "0.0.0.0"
    proxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    proxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((HOST, PORT), proxy.UDPHandler)
    server.serve_forever()




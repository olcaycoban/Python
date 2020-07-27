import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target ="37.247.111.103"

def pscan(port):
    try:
        con = s.connect((target,port))
        banner=s.recv(1024)
        Log = "Port  " + str(port) + "  is open.\n"
        print(Log)
        print(banner)
        dosya=open("Ports.txt","a")
        dosya.write(Log)
        dosya.close()
    except:
        Log = "Port  " + str(port) + "  is closed.\n"
        print(Log)

        dosya = open("Ports.txt", "a")
        dosya.write(Log)
        dosya.close()
"""
for i in range(25,100):
    pscan(i)
"""

pscan(21)
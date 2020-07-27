import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target ="37.247.111.103"

def pscan(port):
    try:
        con = s.connect((target,port))
        banner=s.recv(1024)
        Log = "Port  " + str(port) + "  is open.\n"
        print(Log)
        banner=str(banner).replace("\n","").replace(" ","_")
        dosya=open("Banner.txt","a")
        dosya.write(Log)
        dosya.write(banner)
        dosya.close()
    except:
        pass
pscan(21)
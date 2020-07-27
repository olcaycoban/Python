import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target ="37.247.111.103"

def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False
if pscan(80):
    print('Port', 80, 'is open.')

"""
for x in range(100):
    if pscan(x):
        print('Port',x,'is open.')
    else:
        print('Port',x,'is closed.')
"""
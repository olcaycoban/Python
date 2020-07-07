import socket

s=socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(1)
print(host)
print("Waiting for connectionssssss.......")
conn,address=s.accept()
print("Has been connected",address)

filename=input(str("Please enter the file name"))
file=open(filename,'rb')
file_data=file.read(1024)
conn.send(file_data)
print("Data has been transmitted........")
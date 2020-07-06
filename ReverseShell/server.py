import socket
import sys


def create_socket():
    try:
        global s,port,host
        s=socket.socket()
        host=""
        port=1111
    except socket.error as msg:
        print("Error :",str(msg))

def bind_socket():
    try:
        global s, port, host
        print("Binding the Port: ",str(port))

        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Error",str(msg),"Retryinggggggggg")
        bind_socket()


def socket_accept():
    conn,adress=s.accept()
    print("Connection has been established!!!!!"+"IP: "+adress[0],"------ Port: "+str(adress[1]))
    send_command(conn)
    conn.close()


def send_command(conn):
    while True:
        cmd=input()
        if cmd=='quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response=str(conn.recv(1024),'utf-8')
            print(client_response,end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
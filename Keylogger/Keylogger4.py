from pynput.mouse import Controller ,Listener

def WriteToFile2(x,y):
    print("Current Position {0}".format((x,y)))

with Listener(on_move=WriteToFile2) as F:
    F.join()

"""def WriteToFile3(x,y):
    print("Current Position adsasd")

mouse=Controller()

with Listener(on_click=WriteToFile3) as F:
    F.join()"""
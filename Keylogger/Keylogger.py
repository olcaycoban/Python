import datetime

gun = datetime.datetime.now().strftime("%d")
ay = datetime.datetime.now().strftime("%m")
yil = datetime.datetime.now().strftime("%Y")
saat = datetime.datetime.now().strftime("%H")
dakika = datetime.datetime.now().strftime("%M")

tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

f=open("Log.txt",'w')
f.write("deneme123  {0} \n".format(tarihsaat))
f.close()
f=open("Log.txt",'a')
f.write("deneme123  {0} \n ".format(tarihsaat))
f.close()

f=open("Log.txt",'r')
filess=f.read()
print(filess)
f.close()

with open("Log.txt",'a+') as F:
    F.write("deneme123  {0} \n ".format(tarihsaat))
    F.write("deneme123  {0} \n ".format(tarihsaat))
    filess = F.read()
    print(filess)



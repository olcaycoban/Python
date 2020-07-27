import requests
header={'Cookie': 'PHPSESSID=9salg69n3n77s4op9iebjb5ft1;' }

dosya=open("subdomain.txt","r")
icerik=dosya.read()
dosya.close()

for i in icerik.splitlines():
    subdomain="http://"+str(i)+".yilmazsazevi.com"
    sonuc=requests.get(url=subdomain,header=header)
    print("Dizin :"+i)
    print("Sonuc "+str(sonuc.status_code))

import requests
header={'Cookie': 'PHPSESSID=9salg69n3n77s4op9iebjb5ft1;' }

dosya=open("fuzzing.txt","r")
icerik=dosya.read()
dosya.close()

url="https://www.yilmazsazevi.com"

for i in icerik.splitlines():
    url_istek=url+str(i)
    sonuc=requests.get(url=url_istek,header=header)
    print("Dizin :"+i)
    print("Sonuc "+str(sonuc.status_code))
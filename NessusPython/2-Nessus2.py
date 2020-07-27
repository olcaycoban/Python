import requests

header={"X-ApiKeys": "accessKey=b3933fa96e42de61e71c38c87fbf7c13e4e45c148e7f6a75e16d7e28ea3e4952;" "secretKey=6c0e540595744e45b32cbb58e3db94d9b9e128b157246f428d2a3230282ac3d4;"}
url="https://localhost:8834/scans"

sonuc=requests.get(url=url,headers=header,verify=False)

for i in sonuc.json()['scans']:
    print(str(i['id'])+"\n")
    dosya = open("sonuclar.txt", "a")
    dosya.write(str(i['id'])+"\n")
    dosya.close()
    url2="https://localhost:8834/scans/"+str(i['id'])
    sonuc2=requests.get(url=url2,headers=header,verify=False)
    #print(sonuc2.json())
    for zaafiyet in sonuc2.json()['vulnerabilities']:
        print(zaafiyet['count'])
        print(zaafiyet['plugin_id'])
        print(zaafiyet['plugin_name'])
        print(zaafiyet['plugin_family'])
        dosya = open("sonuclar.txt", "a")
        dosya.write(str(zaafiyet['count'])+"\n")
        dosya.write(str(zaafiyet['plugin_id'])+"\n")
        dosya.write(str(zaafiyet['plugin_name'])+"\n")
        dosya.write(str(zaafiyet['plugin_family'])+"\n")
        dosya.close()
    print("**"*10)
    dosya = open("sonuclar.txt", "a")
    dosya.write(("***"*20)+"\n")
    dosya.close()

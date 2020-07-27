import requests

header={"X-ApiKeys": "accessKey=b3933fa96e42de61e71c38c87fbf7c13e4e45c148e7f6a75e16d7e28ea3e4952;" "secretKey=6c0e540595744e45b32cbb58e3db94d9b9e128b157246f428d2a3230282ac3d4;"}
url="https://localhost:8834/scans"

sonuc=requests.get(url=url,headers=header,verify=False)
"""
for i in sonuc.json()['folders']:
    print(i)
"""
#print(sonuc.json()['scans'])
for i in sonuc.json()['scans']:
    url2="https://localhost:8834/scans/"+str(i['id'])
    sonuc2=requests.get(url=url2,headers=header,verify=False)
    #print(sonuc2.json())
    print(sonuc2.json()['vulnerabilities'])

import requests

header={"X-ApiKeys": "accessKey=b3933fa96e42de61e71c38c87fbf7c13e4e45c148e7f6a75e16d7e28ea3e4952;" "secretKey=6c0e540595744e45b32cbb58e3db94d9b9e128b157246f428d2a3230282ac3d4;"}
url="https://localhost:8834/scans"

sonuc=requests.get(url=url,headers=header,verify=False)

for i in sonuc.json()['scans']:
    print(str(i['id'])+"\n")
    url="https://localhost:8834/scans/"+str(i['id'])
    sonuc = requests.get(url=url, headers=header, verify=False)
    for hostlar in sonuc.json()['hosts']:
        try:
            print("IP : "+str(hostlar['hostname']))
            IP=hostlar['hostname']
            print("Host ID : "+str(hostlar['host_id']))
            url="https://localhost:8834/scans/"+str(i['id'])+"/hosts/"+str(hostlar['host_id'])+"/plugins/11936"  #19506
            zafiyet=requests.get(url=url,headers=header,verify=False)
            plugin_output=zafiyet.json()['outputs'][0]["plugin_output"]
            print(zafiyet.json()['outputs'][0]["plugin_output"])
            Log=str(IP)+"\n"+str(plugin_output)+"\n*********************************************************\n"
            dosya=open("Logs.txt","a")
            dosya.write(Log)
            dosya.close()
        except:
            pass

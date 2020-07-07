import getpass
import socket

kullaniciAdi = getpass.getuser()
bilgisayarAdi = socket.gethostname()
bilgisayarIpAdresi = socket.gethostbyname(socket.gethostname())


sunucuyaGonderilecekMesaj = kullaniciAdi+"___"+bilgisayarAdi+"___"+bilgisayarIpAdresi

istemciSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.128"
port = 23456
Buffer_Boyutu = 1024
istemciSoketi.connect((host, port))
print ("Gonderilecek veri: ", sunucuyaGonderilecekMesaj)
istemciSoketi.send(str.encode(sunucuyaGonderilecekMesaj))
print("Veri sunucuya basarili bir sekilde gonderildi.")
sunucudanGelenMesaj = istemciSoketi.recv(Buffer_Boyutu)
print("Sunucudan Gelen Mesaj: ", sunucudanGelenMesaj)

print("Sunucudan onay mesaji da alindigina gore; istemci tarafinda da baglanti koparilabilir")
istemciSoketi.close()
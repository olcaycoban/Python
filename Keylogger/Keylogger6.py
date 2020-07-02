import smtplib
content=open("Log3.txt",'a')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("kpasseras1234@gmail.com","olcay1453!")
server.sendmail("kpasseras1234@gmail.com","olcaycoban3737@gmail.com",content)
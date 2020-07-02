import numpy as np
import matplotlib.pyplot as plt

x=["Amerika","Çin","Japonya","Almanya","İngiltere","Fransa"]
y=["78000","65000","43000","60000","54000","23000"]
z=["12000","45","62"]

#plt.plot(x,y,"r")
#plt.show();

plt.subplot(1,2,1)
plt.plot(x,y,"r--")
plt.tight_layout()
plt.show()

plt.subplot(1,2,2)
plt.plot(x,y)
plt.tight_layout()
plt.show()


f=plt.figure(figsize=(5,5))
axes=f.add_axes([0.1,0.1,0.9,0.9])
axes.plot(x,y)
axes.set_xlabel("Ülkeler")
axes.set_ylabel("Milli Gelirler")
axes.set_title("Ülkelere Göre Milli Gelirler")
plt.show()

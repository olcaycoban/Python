import numpy as np
import matplotlib.pyplot as plt

x=["Amerika","Çin","Japonya","Almanya","İngiltere","Fransa"]
y=[230000,65000,40000,73000,54000,90000]
z=[120000,45000,62000,45000,85000,80000]


f=plt.figure()
ax=f.add_axes([0.1,0.1,0.9,0.9])
ax.set_xlabel("Ülkeler")
ax.set_ylabel("Gelirler")
#ax2=f.add_axes([0.6,0.6,0.7,0.8])
#ax2.plot(x,z)
ax.plot(x,y,'r-o',label="Milli Gelir",)
ax.plot(x,z,"g-",label="Cari Açık")
ax.legend(loc=1)
plt.show()
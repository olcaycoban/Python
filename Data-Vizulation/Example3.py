import numpy as np
import matplotlib.pyplot as plt

x=["Amerika","Çin","Japonya","Almanya","İngiltere","Fransa"]
y=[23000,65000,40000,73000,54000,90000]

f=plt.figure()
axes1=f.add_axes([0.1,0.1,0.9,0.9])
axes2=f.add_axes([0.5,0.5,0.4,0.4])
axes1.plot(x,y,"b",linewidth=1,linestyle="--",marker="o",markersize=10,markerfacecolor="red",
                    markeredgewidth=4,markeredgecolor="blue",alpha=0.5)
axes1.set_xlabel("Ülkeler")
axes1.set_ylabel("Gelirler")
axes1.set_xlim([0,3])
#plt.tight_layout()
axes2.plot(x,y,"r")
plt.show()
f.savefig("4dasdsad.png")

import numpy as np
import matplotlib.pyplot as plt

x = [2015,2016,2017,2018,2019]
y1 = [24000,45000,39000,60000,65000]
y2 = [15000,6000,12000,24000,80000]
y3 = [34000,4000,39000,15000,45200]

y = np.vstack([y1, y2, y3])

labels = ["Amerika ", "Rusya", "Çin"]
fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3, labels=labels)
ax.legend(loc='upper left')
plt.show()

fig, ax = plt.subplots()
ax.stackplot(x, y)
plt.xlabel("Ülkeler")
plt.ylabel("Yıllar")
plt.title("Ülkelerin Milli Gelirleri")
plt.show()
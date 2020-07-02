import matplotlib.pyplot as plt

labels = 'Türkiye', 'Rusya', 'ABD', 'Iran'
sizes = [15, 30, 45, 10]
explode = (0.2, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.7f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
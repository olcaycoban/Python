import matplotlib.pyplot as plt
import pandas as pd

c=pd.read_csv("dünya.csv")
#plt.scatter(c["Ülke"],c["Kişi Başına"])
#plt.hist(c["Kişi Başına"],bins=5)
plt.step(c["Ülke"],c["Kişi Başına"])
plt.show()
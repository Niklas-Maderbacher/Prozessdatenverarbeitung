import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

unemp = pd.read_csv("./01_unemp.csv", sep=",")
techscore = pd.read_csv("./03_techScore.csv", sep=",")

masks = unemp['Country Code']
data_unemp = []

for mask in masks:
    print(mask)

print(unemp)

#x = 4 + np.random.normal(0, 2, 24)
#y = 4 + np.random.normal(0, 2, len(x))
# size and color:
#sizes = np.random.uniform(15, 80, len(x))
#colors = np.random.uniform(15, 80, len(x))

# plot
#fig, ax = plt.subplots()
#
#ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
#
#ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#       ylim=(0, 8), yticks=np.arange(1, 8))
#
#plt.show()

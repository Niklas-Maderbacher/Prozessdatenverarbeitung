import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./01_unemp.csv", sep=",")

mask = df['Country Code'].isin(['AUT'])
aut_data = df[mask]

years = []
for i in range(1991, 2022):
    years.append(str(i))

unemp = []
for year in years:
    unemp.append(aut_data[year])

print(unemp)

# make data
x = years
y = unemp

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.title("Unemployment in Austria")
plt.xlabel("Year")
plt.ylabel("Percentage")

plt.show()
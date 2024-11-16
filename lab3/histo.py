# Import necessary libraries
import numpy as np              # For working with numerical arrays
import pandas as pd             # *NEW* For easily importing spreadsheet data
import matplotlib.pyplot as plt # For easy plotting

data = pd.read_csv("data.csv", index_col='Trial')

pull_force_values = data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 556.4) & (data['Date'] == '10/31/24')]['Pull-Force']


fig1 = plt.figure()
#plt.grid()
plt.hist(pull_force_values, bins=9, color='blue', alpha=0.7, edgecolor='black')

# Define tick positions starting from 1.4 with a step of 4/45
step = 4/45
ticks = np.arange(1.4, 2.2 + step, step)

# Generate tick labels in mixed number format
'''tick_labels = []
for x in ticks:
    whole_number = int(x)
    numerator = int(round((x - whole_number) * 45))
    if numerator == 0:
        tick_labels.append(f"${whole_number}$")
    else:
        tick_labels.append(f"${whole_number} \\frac{{{numerator}}}{{45}}$")


plt.xticks(ticks, tick_labels)'''
plt.xlabel("Static Pull Force (N)")
plt.ylabel("# of Trials (out of 100)")
plt.savefig("histo.svg", format = 'svg')
#plt.show()

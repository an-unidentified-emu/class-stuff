# Import necessary libraries
import numpy as np              # For working with numerical arrays
import pandas as pd             # *NEW* For easily importing spreadsheet data
import matplotlib.pyplot as plt # For easy plotting

data = pd.read_csv("data.csv", index_col='Trial')

pull_force_values = data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] == 5556.4) & (data['Date'] == '10/31/24')]['Pull-Force']


fig1 = plt.figure()
#plt.grid()
plt.hist(pull_force_values, bins=6, color='blue', edgecolor='black')
plt.xlabel("Pull Force (N)")
plt.ylabel("# of Trials")
plt.savefig("histo2.svg", format = 'svg')
#plt.show()

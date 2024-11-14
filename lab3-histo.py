# Import necessary libraries
import numpy as np              # For working with numerical arrays
import pandas as pd             # *NEW* For easily importing spreadsheet data
import matplotlib.pyplot as plt # For easy plotting

SLOPE_UNC = 0.0117
data = pd.read_csv("data.csv", index_col='Trial')
# Filter rows based on TypeofForce, Angle, and Mass, then select Pull-Force column 
#pull_force_values = data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 556.4)]['Pull-Force']
Gforce = list(set(data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0)]['Gravity-Force']))
Gforce.sort()
Gforce = np.array(Gforce, dtype=np.float64)/1000

means = [data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 556.4)]['Pull-Force'].mean(), \
         data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 956.4)]['Pull-Force'].mean(), \
         data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 5556.4)]['Pull-Force'].mean(), \
         data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 10556.4)]['Pull-Force'].mean()]

stds =  [data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 556.4)]['Pull-Force'].std(), \
         data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 956.4)]['Pull-Force'].std(), \
         data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 5556.4)]['Pull-Force'].std(), \
         data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 10556.4)]['Pull-Force'].std()]

print(means)
print(stds)

pull_force_values = data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0)]['Pull-Force']
temp = data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0)]['Un-Force']


fig1 = plt.figure()
plt.hist(pull_force_values, bins=int(np.sqrt(len(pull_force_values))), color='red', edgecolor='black')
plt.xlabel("Pull Force (N)")
plt.ylabel("# of Trials")
plt.show()

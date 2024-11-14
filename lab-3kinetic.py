# Import necessary libraries
import numpy as np              # For working with numerical arrays
import pandas as pd             # *NEW* For easily importing spreadsheet data
import matplotlib.pyplot as plt # For easy plotting

SLOPE_UNC = 0.0117
DATE = '10/31/24'
data = pd.read_csv("data.csv", index_col='Trial')
# Filter rows based on TypeofForce, Angle, and Mass, then select Pull-Force column 
#pull_force_values = data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 556.4)]['Pull-Force']
Gforce = list(set(data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0)]['Gravity-Force']))
Gforce.sort()
Gforce = np.array(Gforce, dtype=np.float64)/1000

bMeans = [
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean()
]

bStds = [
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std()
]

cMeans = [
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean()
]

cStds = [
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std()
]


static_pull_force_values = data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0)]['Pull-Force']
kinetic_pull_force_values = data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0)]['Pull-Force']
temp = data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0)]['Un-Force']

slope = np.sum(Gforce * cMeans) / np.sum(Gforce**2)
slope_upper = slope + SLOPE_UNC
slope_lower = slope - SLOPE_UNC

Gforce_extended = np.linspace(0, max(Gforce) * 1.5, 100)

y_fit = slope * Gforce_extended
y_fit_lower = slope_lower * Gforce_extended
y_fit_upper = slope_upper * Gforce_extended
print(slope)
fig1 = plt.figure()
plt.errorbar(Gforce, cMeans, cStds, fmt='.', color='red')
plt.plot(Gforce_extended, y_fit, color = 'green')
# Plot thin lines for upper and lower bounds
plt.plot(Gforce_extended, y_fit_upper, color='blue', linestyle='--', linewidth=0.8)
plt.plot(Gforce_extended, y_fit_lower, color='blue', linestyle='--', linewidth=0.8)
plt.grid(True,'both','both')
# Fill the area between the upper and lower bounds with a gray shade
plt.fill_between(Gforce_extended, y_fit_lower, y_fit_upper, color='gray', alpha=0.3)

plt.xlim(0,125)
plt.ylim(0,45)

plt.xlabel("Force of Gravity (N)")
plt.ylabel("Static Pull Force (N)")

plt.show()
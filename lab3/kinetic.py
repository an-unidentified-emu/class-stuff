# Import necessary libraries
import numpy as np              # For working with numerical arrays
import pandas as pd             # *NEW* For easily importing spreadsheet data
import matplotlib.pyplot as plt # For easy plotting

SLOPE_UNC_B = 0.0246
SLOPE_UNC_C = 0.0221
ANGLE = 7.86

DATE = '10/31/24'
data = pd.read_csv("data.csv", index_col='Trial')
# Filter rows based on TypeofForce, Angle, and Mass, then select Pull-Force column 
#pull_force_values = data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0) & (data['Mass'] == 556.4)]['Pull-Force']
Gforce = list(set(data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0)]['Gravity-Force']))
Gforce.sort()
Gforce = np.array(Gforce, dtype=np.float64)/1000

fMeans = [
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean()
]

fStds = [
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std()
]

aMeans = [
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean()
]

aStds = [
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].std()
]


# Static Force
static_pull_force_values = data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0)]['Pull-Force']
slope = np.sum(Gforce * fMeans) / np.sum(Gforce**2)
slope_upper = slope + SLOPE_UNC_B
slope_lower = slope - SLOPE_UNC_B

temp = Gforce*np.sin(np.deg2rad(7.86))
Gforce = Gforce*np.cos(np.deg2rad(7.86))
aMeans -= temp

Gforce_extended = np.linspace(0, max(Gforce) * 1.5, 100)

y_fit = slope * Gforce_extended
y_fit_lower = slope_lower * Gforce_extended
y_fit_upper = slope_upper * Gforce_extended
print(slope)
fig1 = plt.figure()

# Static force error bars and line of best fit
plt.errorbar(Gforce, fMeans, fStds, fmt='.', color='red', label='0 Degree Data')
plt.plot(Gforce_extended, y_fit, color='red', label=f'0 Degree Fit \ny={slope:.2f} ± {SLOPE_UNC_B}x')
plt.plot(Gforce_extended, y_fit_upper, color='red', linestyle='--', linewidth=0.8)
plt.plot(Gforce_extended, y_fit_lower, color='red', linestyle='--', linewidth=0.8)
plt.fill_between(Gforce_extended, y_fit_lower, y_fit_upper, color='gray', alpha=0.3)

# Kinetic Force
kinetic_pull_force_values = data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0)]['Pull-Force']
slope = np.sum(Gforce * aMeans) / np.sum(Gforce**2)
slope_upper = slope + SLOPE_UNC_C
slope_lower = slope - SLOPE_UNC_C

Gforce_extended = np.linspace(0, max(Gforce) * 1.5, 100)

y_fit = slope * Gforce_extended
y_fit_lower = slope_lower * Gforce_extended
y_fit_upper = slope_upper * Gforce_extended
print(slope)

# Kinetic force error bars and line of best fit
plt.errorbar(Gforce, aMeans, aStds, fmt='.', color='green', label='7.86 Degree Data')
plt.plot(Gforce_extended, y_fit, color='green', label=f'7.86 Degree Fit\ny={slope:.2f} ± {SLOPE_UNC_C}x')
plt.plot(Gforce_extended, y_fit_upper, color='green', linestyle='--', linewidth=0.8)
plt.plot(Gforce_extended, y_fit_lower, color='green', linestyle='--', linewidth=0.8)
plt.fill_between(Gforce_extended, y_fit_lower, y_fit_upper, color='gray', alpha=0.3)

# General Graph stuff
plt.legend(loc='upper left', fontsize='small', frameon=True)
plt.xlim(0,120)
plt.ylim(0,45)
plt.grid(True,'both','both')
plt.xlabel("Normal Force (N)")
plt.ylabel("Friction Force (N)")
plt.savefig("kinetic-both.svg", format = 'svg')
#plt.show()
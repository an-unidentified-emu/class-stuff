# Import necessary libraries
import numpy as np              # For working with numerical arrays
import pandas as pd             # *NEW* For easily importing spreadsheet data
import matplotlib.pyplot as plt # For easy plotting

SLOPE_UNC_B = 0.0117
SLOPE_UNC_C = 0.0246
ANGLE = 7.86
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

cMeans = [
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean()
]

bMeans2 = [
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == ANGLE) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == ANGLE) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == ANGLE) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'B') & (data['Angle'] == ANGLE) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean()
]

cMeans2 = [
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] ==   556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] ==   956.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] ==  5556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean(),
    data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE) & (data['Mass'] == 10556.4 ) & (data['Date'] == DATE)] ['Pull-Force'].mean()
]

# Static Force
'''static_pull_force_values = data[(data['TypeofForce'] == 'B') & (data['Angle'] == 0)]['Pull-Force']
slope = np.sum(Gforce * bMeans) / np.sum(Gforce**2)

static_pull_force_values2 = data[(data['TypeofForce'] == 'B') & (data['Angle'] == ANGLE)]['Pull-Force']
slope2 = np.sum(Gforce * bMeans2) / np.sum(Gforce**2)

kinetic_pull_force_values = data[(data['TypeofForce'] == 'C') & (data['Angle'] == 0)]['Pull-Force']
slope = np.sum(Gforce * cMeans) / np.sum(Gforce**2)

kinetic_pull_force_values2 = data[(data['TypeofForce'] == 'C') & (data['Angle'] == ANGLE)]['Pull-Force']
slope2 = np.sum(Gforce * cMeans2) / np.sum(Gforce**2)'''

# Combine all data into a table format
data_table = {
    "Gforce": Gforce,
    "bMeans": bMeans,
    "cMeans": cMeans,
    "bMeans (Angle)": bMeans2,
    "cMeans (Angle)": cMeans2
}

# Convert to a DataFrame
df = pd.DataFrame(data_table)

# Display the table using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, loc='center')

plt.title('Pull-Force Averages by Gforce')
plt.savefig("suck.png")
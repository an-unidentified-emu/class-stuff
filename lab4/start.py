import numpy as np             
import pandas as pd            
import matplotlib.pyplot as plt
angle = 45
data = pd.read_csv("raw.csv", index_col='Trial')

angles = [30, 45, 60]
x = np.arange(1, 6)
# Initialize arrays
Measured = np.zeros(len(angles))
Theoretical = np.zeros(len(angles))

Measured = []
Theoretical = []

# Loop through each angle and filter the data
for angle in angles:
    Measured.append(data[data['Angle'] == angle]['M-Distance'].to_numpy())
    Theoretical.append(data[data['Angle'] == angle]['T-Distance'].to_numpy())

Measured_std = [np.full_like(arr, np.std(arr, ddof=0)) for arr in Measured]
Theoretical_std = [np.full_like(arr, np.std(arr, ddof=0)) for arr in Theoretical]

fig, axs = plt.subplots(3, 1, figsize=(5, 10), sharey="row")

# Left subplot
axs[0].errorbar(x, Measured[0], Measured_std[0], fmt='.', color='red', label='Measured')
axs[0].errorbar(x, Theoretical[0], Theoretical_std[0], fmt='.', color='blue', label='Theoretical')
axs[0].set_title("30 degrees")
axs[0].legend()
axs[0].set_ylabel("Distance")

# Middle subplot
axs[1].errorbar(x, Measured[1], Measured_std[1], fmt='.', color='red', label='Measured')
axs[1].errorbar(x, Theoretical[1], Theoretical_std[1], fmt='.', color='blue', label='Theoretical')
axs[1].set_title("45 degrees")
axs[1].set_xlabel("Trial")

# Right subplot
axs[2].errorbar(x, Measured[2], Measured_std[2], fmt='.', color='red', label='Measured')
axs[2].errorbar(x, Theoretical[2], Theoretical_std[2], fmt='.', color='blue', label='Theoretical')
axs[2].set_title("60 degrees")

# General layout
for ax in axs:
    ax.grid(True)

plt.tight_layout()
plt.savefig("start.svg", format = 'svg')
plt.show()
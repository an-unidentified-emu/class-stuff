import numpy as np             
import pandas as pd            
import matplotlib.pyplot as plt
angle = 45
data = pd.read_csv("newData.csv", index_col='Trial')

angles = [30, 45, 60]
x = np.arange(1, 6)
x_extended = np.arange(-1,8)
# Initialize arrays
Measured = np.zeros(len(angles))
Theoretical = np.zeros(len(angles))

Measured = []
Theoretical = []

# Loop through each angle and filter the data
for angle in angles:
    Measured.append(data[data['Angle'] == angle]['TapeDist'].to_numpy())
    Theoretical.append(data[data['Angle'] == angle]['TimeDist'].to_numpy())

Measured_std = [np.full_like(arr, np.std(arr, ddof=0)) for arr in Measured]
Theoretical_std = [np.full_like(arr, np.std(arr, ddof=0)) for arr in Theoretical]

Measured_mean = [np.pad(np.full_like(arr, np.mean(arr)), (0,4),constant_values=np.mean(arr)) for arr in Measured]
Theoretical_mean = [np.pad(np.full_like(arr, np.mean(arr)), (0,4),constant_values=np.mean(arr)) for arr in Theoretical]

fig, axs = plt.subplots(3, 1, figsize=(5, 10), sharey="row")

# Subplots
for i in range(0,3):
    # Measured
    upper = [Measured_mean[i][j] + Measured_std[i][1] for j in range(len(Measured_mean[i]))]
    lower = [Measured_mean[i][j] - Measured_std[i][1] for j in range(len(Measured_mean[i]))]
    axs[i].errorbar(x,    Measured[i], fmt='.', color='red', label='Measured')
    axs[i].plot(x_extended, Measured_mean[i], color = 'red',linestyle='--')
    axs[i].plot(x_extended, upper, color='green', linestyle='--', linewidth=0.8)
    axs[i].plot(x_extended, lower, color='green', linestyle='--', linewidth=0.8)
    axs[i].fill_between(x_extended, lower, upper, color='gray', alpha=0.3)

    # Theoretical
    upper = [Theoretical_mean[i][j] + Theoretical_std[i][1] for j in range(len(Theoretical_mean[i]))]
    lower = [Theoretical_mean[i][j] - Theoretical_std[i][1] for j in range(len(Theoretical_mean[i]))]
    axs[i].errorbar(x, Theoretical[i], fmt='.', color='blue', label='Theoretical')
    axs[i].plot(x_extended, Theoretical_mean[i], color = 'blue',linestyle='--')
    axs[i].plot(x_extended, upper, color='green', linestyle='--', linewidth=0.8)
    axs[i].plot(x_extended, lower, color='green', linestyle='--', linewidth=0.8)
    axs[i].fill_between(x_extended, lower, upper, color='gray', alpha=0.3)

    # Graph Stuff
    axs[i].set_title(f"{(i*15+30)} degrees")
    axs[i].legend()
    axs[i].grid(True)
    axs[i].set_xlabel("Trial")
    axs[i].set_ylabel("Distance")
    axs[i].set_xlim(0,6)

plt.tight_layout()
plt.savefig("timeDist.svg", format = 'svg')
plt.show()
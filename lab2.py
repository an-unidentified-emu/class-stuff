import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the raw data from Excel (assumes column 3 defines graph location, column 6 is y-values, and column 7 is error)
df = pd.read_excel('data.xlsx')

# Extract the columns of interest
x_vals = df.iloc[:, 8]  # Assuming the x-values are in column 9 (0-indexed in Python)
graph_positions = df.iloc[:, 2]  # Graph position (0: left, 1: middle, 2: right)
y_vals = df.iloc[:, 5]   # y-values
error_vals = df.iloc[:, 6]  # Vertical error bars

# Filter data for the specific graph (position == 2)
graph_data = graph_positions == 2

# Calculate mean and standard deviation of y-values
mean_y = np.mean(y_vals[graph_data])
std_y = np.std(y_vals[graph_data])

# Get x-axis range for horizontal lines
x_min, x_max = 0, 30

# Plot the data with error bars
plt.figure()
plt.errorbar(x_vals[graph_data], y_vals[graph_data], yerr=error_vals[graph_data], fmt='none', capsize=3)
plt.plot(x_vals[graph_data], y_vals[graph_data], '*', markersize=6)
plt.ylabel('Acceleration (EMU/s^2)')
plt.xlabel('Student Groups')
plt.ylim(2000, 4500)  # Set y-axis range
plt.xlim(15, 25)
plt.xticks([])  # Hide x-axis values
plt.grid(True)

# Add horizontal lines for mean and standard deviation using plot
plt.plot([x_min, x_max], [mean_y, mean_y], 'r-', linewidth=2)  # Red line for the mean
plt.plot([x_min, x_max], [mean_y + std_y, mean_y + std_y], 'g--', linewidth=2)  # Green dashed line for mean + 1 SD
plt.plot([x_min, x_max], [mean_y - std_y, mean_y - std_y], 'g--', linewidth=2)  # Green dashed line for mean - 1 SD

# Add a legend for the mean and standard deviation lines
plt.legend(['Mean', 'Mean ± 1 Std Dev'])

# Save the figure
plt.savefig("lab2.png", format = 'png')
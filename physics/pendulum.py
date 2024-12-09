import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# populate the code below with your input values
m = 1     # pendulum bob mass (kg)
l = 1     # pendulum cord length (m)
g = 9.81  # acceleration of gravity (m/s^2)
b = 0     # damping coefficient (kg/s)
tsim = 10  # simulation time (seconds)
disp = 45  # initial condition (displacement angle in degrees)

# Convert initial displacement to radians
ic = disp * (np.pi / 180)

# Define the system of differential equations
def pendulum_ode(t, x):
    return [x[1], 1/m * (-b * x[1] - m * (g / l) * np.sin(x[0]))]

# Generate vector field
x1 = np.linspace(-np.pi, np.pi, 80)
x2 = np.linspace(-np.pi, np.pi, 80)
X, Y = np.meshgrid(x1, x2)
u = np.zeros(X.shape)
v = np.zeros(Y.shape)

t = 0
for i in range(X.size):
    Xsys = pendulum_ode(t, [X.ravel()[i], Y.ravel()[i]])
    u.ravel()[i] = Xsys[0]
    v.ravel()[i] = Xsys[1]

# Plot the vector field
plt.figure(1)
plt.quiver(X, Y, u, v, color='r')
plt.grid(True)
plt.xlabel('x_2 velocity')
plt.ylabel('x_1 displacement')
plt.title('Phase portrait')

# Solve the system using solve_ivp
sol = solve_ivp(pendulum_ode, [0, tsim], [0, ic], dense_output=True)
ts = sol.t
ys = sol.y

# Plot the trajectory
plt.plot(ys[0, :], ys[1, :], 'b', linewidth=2)
plt.plot(ys[0, 0], ys[1, 0], 'go')  # Starting point
plt.plot(ys[0, -1], ys[1, -1], 'k*')  # Ending point
plt.plot(0, 0, 'yd')  # Origin
plt.legend(['Vector field', 'Trajectory', 'Starting point', 'End point', 'Origin'])
plt.axis([-0.5 * np.pi, 0.5 * np.pi, -0.5 * np.pi, 0.5 * np.pi])
plt.show()

# Plot angle and angular velocity over time
plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(ts, ys[1, :])
plt.xlabel('time (s)')
plt.ylabel('angle (rad)')
plt.title('Simple damped pendulum')

plt.subplot(2, 1, 2)
plt.plot(ts, ys[0, :])
plt.xlabel('time (s)')
plt.ylabel('rate (rad/s)')
plt.show()

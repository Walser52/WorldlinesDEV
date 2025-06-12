import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define the symbolic variables and parametric equations
t = sp.Symbol('t')
x = sp.cos(t)
y = sp.sin(t)

# Convert the parametric equations to a numerical function
f_x = sp.lambdify(t, x, 'numpy')
f_y = sp.lambdify(t, y, 'numpy')

# Generate the values for the curve
t_values = np.linspace(0, 2 * np.pi, 400)
x_values = f_x(t_values)
y_values = f_y(t_values)

# Set up the plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
line, = plt.plot(x_values, y_values, lw=2)
dot, = plt.plot([], [], 'ro')  # The red dot indicating the position

# Set plot limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Define the slider axis and create the slider
axcolor = 'lightgoldenrodyellow'
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor=axcolor)
slider = Slider(ax_slider, 't', 0, 2 * np.pi, valinit=0)

# Update function for the slider
def update(val):
    t_val = slider.val
    x_val = f_x(t_val)
    y_val = f_y(t_val)
    dot.set_data([x_val], [y_val])  # Update the dot position
    fig.canvas.draw_idle()

# Set the update function to the slider
slider.on_changed(update)

# Display the plot
plt.show()


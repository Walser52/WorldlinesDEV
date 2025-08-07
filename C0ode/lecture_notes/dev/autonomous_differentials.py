import plotly.express as px
import pandas as pd
import numpy as np

# Define the function f(y) from the autonomous equation dy/dx = f(y)
# Example: dy/dx = y**2 - 4
def f(y):
    return y**2 - 4

# Create a range of y values
y_values = np.linspace(-4, 4, 100)
f_y_values = f(y_values)

# Create a pandas DataFrame for Plotly Express
df = pd.DataFrame({'y': y_values, 'f(y)': f_y_values})

# Create a line plot
fig = px.line(df, x='y', y='f(y)',
              title='Plot of f(y) for $dy/dx = y^2 - 4$',
              labels={'y': 'y (Dependent Variable)', 'f(y)': 'Slope (dy/dx)'})

# Add a horizontal line at y=0 to highlight the equilibrium points
fig.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Equilibrium Points where f(y) = 0", annotation_position="bottom right")

# Customize the plot layout
fig.update_layout(
    xaxis_title='y',
    yaxis_title='f(y) = dy/dx',
    autosize=False,
    width=600,
    height=600,
    margin=dict(t=50, b=50, l=50, r=50)
)

# Show the plot
fig.show()


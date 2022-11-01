import numpy as np
import plotly.graph_objects as go

x = np.arange(0,1,0.01)
y = np.sin(2*np.pi*x)

print("Hola mundo!")
print(x)
print(y)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x,y=y, mode="markers"))
fig.show()

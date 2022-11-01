import numpy as np
import plotly.graph_objects as go

x = np.arange(0,1,0.01)
f1 = np.sin(2*np.pi*x)
f2 = np.cos(2*np.pi*x)


#print("Hola mundo!")
#print(x)
#print(y)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x,y=f1, mode="markers"))
fig.add_trace(go.Scatter(x=x,y=f2, mode="markers"))

fig.show()

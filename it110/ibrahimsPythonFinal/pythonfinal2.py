import MySQLdb
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
py.sign_in("ibrahim713", "0LRxZRWw04gEYwULmu8e")

trace0 = go.Scatter(
x=[1, 2, 3, 4],
y=[10, 11, 12, 13],
mode='markers',
marker=dict(
size=[40, 60, 80, 100],
)
)
data = [trace0]
py.iplot(data, filename='bubblechart-size')

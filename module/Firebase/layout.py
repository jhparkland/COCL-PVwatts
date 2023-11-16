import dash
from dash import Dash, html, dcc
from dash.dependencies import Output, Input, State
import pyrebase


app = Dash(__name__)

app.layout = html.Div([
    html.H2(children='Location Info'),
    html.Div(id='location-output'),
    dcc.Input(id='dummy-input', type='hidden', value='constant-value'),

    html.H2(children='Solar Power Graph'),
    html.Label("Select Month:"),
    dcc.Dropdown(
        id='month-dropdown',
        options=[{'label': f'Month : {month}', 'value': month} for month in range(1, 13)],
        value=1
    ),

    html.Label("Select Day:"),
    dcc.Dropdown(
        id='day-dropdown',
        options=[{'label': f'Day : {day}', 'value': day} for day in range(1, 32)],
        value=1
    ),

    html.Button('OK', id='ok-button', n_clicks=0),

    dcc.Graph(id='solar-power-graph'),
])
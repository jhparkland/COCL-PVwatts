from dash.dependencies import Output, Input, State
from layout import app
from firebase import FirebaseManager

firebase_manager = FirebaseManager()
db = firebase_manager.db

@app.callback(
    Output('location-output', 'children'),
    Input('dummy-input', 'value')
)
def update_location(dummy_value):
    data = db.child("information").get().val()

    if data:
        entry = data[0]
        location_info = {
            "Requested Location": entry.get("Requested Location"),
            "Latitude (DD)": entry.get("Latitude (DD)"),
            "Longitude (DD)": entry.get("Longitude (DD)")
        }
        return f'<Requested Location>: {location_info["Requested Location"]}, <Latitude>: {location_info["Latitude (DD)"]}, <Longitude>: {location_info["Longitude (DD)"]}'
    else:
        return 'No data available'

@app.callback(
    Output('solar-power-graph', 'figure'),
    [Input('ok-button', 'n_clicks')],
    [State('month-dropdown', 'value'),
     State('day-dropdown', 'value')]
)
def update_graph(n_clicks, selected_month, selected_day):
    data = db.child("pvwatts").get().val()

    if data and n_clicks > 0:
        dc_output_data = []
        for entry in data:
            if entry.get("Month") == selected_month and entry.get("Day") == selected_day:
                dc_output_data.append(entry.get("DC Array Output (W)", 0))

        figure = {
            'data': [
                {'x': list(range(len(dc_output_data))), 'y': dc_output_data, 'type': 'line', 'name': 'Solar Power Generation'},
            ],
            'layout': {
                'title': f'Solar Power Generation for {selected_month}/{selected_day}',
                'xaxis': {'title': 'Time (hours)'},
                'yaxis': {'title': 'Solar Power (W)'},
            }
        }
        return figure
    else:
        return {'data': []}

if __name__ == '__main__':
    app.run_server(debug=True)

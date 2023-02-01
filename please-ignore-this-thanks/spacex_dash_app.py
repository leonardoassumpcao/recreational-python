# Import required libraries
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

spacex_df = pd.read_csv("spacex_launch_dash.csv")
spacex_df.columns = ['unnamed_0', 'flight_number', 'launch_site', 'class', 'payload_mass_kg', 'booster_version', 'booster_version_category']
spacex_df.pop('unnamed_0')

max_payload = spacex_df["payload_mass_kg"].max()
min_payload = spacex_df["payload_mass_kg"].min()


app = dash.Dash(__name__)  # Creates a dash application

# Create an app layout:
app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40},
        ),
        # TASK 1:
        # Add a dropdown list to enable Launch Site selection
        dcc.Dropdown(
            id = 'site-dropdown',
            value = 'ALL',  # The default select value is for ALL sites.
            placeholder = 'Select a Launch Site here',
            searchable = True,
            options = [{'label': 'All Sites', 'value': 'ALL'}] + [{"label":k, "value":k} for k in spacex_df.launch_site.unique()]
        ),
        html.Br(),

        # TASK 2:
        # Add a pie chart to show the total successful launches count for all sites.
        # If a specific launch site was selected, show the Success vs. Failed counts for the site.
        html.Div(dcc.Graph(id="success-pie-chart")),
        html.Br(),
        html.P("Payload range (Kg):"),
        # TASK 3: Add a slider to select payload range.
        dcc.RangeSlider(
            id = 'payload-slider',
            min = 0,
            max = 10000,
            step = 1000,
            value = [min_payload, max_payload]
        ),

        # TASK 4: Add a scatter chart to show the correlation between payload and launch success
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ]
)

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_graph(entered_site):
    if entered_site == 'ALL':
        figure = px.pie(spacex_df, values='class', names='launch_site', title='Total Success Launches Per Site')
        return figure
    else:
        ii = spacex_df['launch_site'] == entered_site
        filtered_df = spacex_df[ii].groupby('launch_site class'.split()).size()
        filtered_df = filtered_df.reset_index(name='class count', inplace=False)
        # figure = px.pie(filtered_df, values='class count', names='class', title=f'Success Rate for Site {entered_site}')
        title, co = f'Success Rate for Site {entered_site}', {'class': '0 1'.split()}
        figure = px.pie(filtered_df, values='class count', names='class', color='class', title=title, category_orders=co, color_discrete_sequence=['red', 'green'])
        return figure

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value'),
    Input(component_id='payload-slider', component_property='value')
)
def get_scatter(entered_site, payload_range):
    ii = spacex_df['payload_mass_kg'].between(payload_range[0], payload_range[1])
    if entered_site == 'ALL':
        filtered_df = spacex_df[ii]
        figure = px.scatter(filtered_df, x='payload_mass_kg', y='class', color='booster_version_category', title='Correlation between Payload and Success for All Sites')
        return figure
    else:
        jj = spacex_df['launch_site'] == entered_site
        filtered_df = spacex_df[ii & jj]
        figure = px.scatter(filtered_df, x='payload_mass_kg', y='class', color='booster_version_category', title=f'Correlation between Payload and Success for Site {entered_site}')
        return figure


if __name__ == "__main__":
    app.run_server()  # Runs the app.



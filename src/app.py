import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Load the flights dataset
flights = pd.read_csv("../data/flights.csv")

# Define the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.YETI])

# Define the layout
app.layout = html.Div([
    html.H1("🛫️ European Flight Data 🛬️"),
    html.Label("Select a Year 🕙"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": year, "value": year} for year in flights["Year"].unique()],
        value=flights["Year"].min()
    ),
    html.Label("Select a European Country 🗺️"),
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in flights["Country"].unique()],
        value=flights["Country"].iloc[0]
    ),
    dcc.Graph(id="airport-plot"),
    dcc.Graph(id="flight-plot")
], className="container",
    style={'backgroundColor': '#ADD8E6'})


# Define the callback to update the airport plot
@app.callback(
    dash.dependencies.Output("airport-plot", "figure"),
    [dash.dependencies.Input("year-dropdown", "value"),
     dash.dependencies.Input("country-dropdown", "value")]
)
def update_airport_plot(year, country):
    # Filter the data by year and country
    data = flights[(flights["Year"] == year) & (flights["Country"] == country)]
    
    # Group the data by airport and sum the total flights for each airport in the selected country
    grouped_data = data.groupby("Airport").sum().reset_index()
    
    # Sort the data by total flights in decreasing order
    grouped_data = grouped_data.sort_values("Total", ascending=False)
    
    # Create a bar chart of the total number of flights for each airport
    fig = px.bar(grouped_data, x="Airport", y="Total", 
                 title=f"What is the Busiest Airport in {country} ✈️ {year}",
                 text=grouped_data["Total"].tolist(),
                 color="Airport",
                 color_continuous_scale=px.colors.sequential.Plasma)
    
    # Update the layout
    fig.update_layout(xaxis_title="Airport", yaxis_title="Total Flights")
    
    return fig

# Define the callback to update the flight plot
@app.callback(
    dash.dependencies.Output("flight-plot", "figure"),
    [dash.dependencies.Input("year-dropdown", "value"),
     dash.dependencies.Input("country-dropdown", "value")]
)
def update_flight_plot(year, country):
    # Filter the data by year and country
    data = flights[(flights["Year"] == year) & (flights["Country"] == country)]
    
    # Group the data by month and sum the departure and arrival flights for all airports in the selected country
    grouped_data = data.groupby("Month").sum().reset_index()
    
    # Create a line plot of the monthly number of departure and arrival flights
    fig = px.line(grouped_data, x="Month", y=["Departure", "Arrival", "Total"],
                  title=f"What is the Busiest Flying Month in {country} 🛩️ {year}")
    
    # Update the layout
    fig.update_layout(xaxis_title="Month", yaxis_title="Number of Flights")
    
    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
#import pandas as pd
#import plotly.graph_objects as go
#from dash.dependencies import Input, Output
iris = px.data.iris()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.H1(children="Scatter Plot"),

    html.Div(children="This plot is from iris data"),

    dcc.Graph(
        id='example-graph',
        figure=px.scatter(iris, x='sepal_width', y = 'sepal_length',
                          color="species", size="petal_length",
                          hover_data=['petal_width']),

    )



])



if __name__=='__main__':
    app.run_server(debug=True)
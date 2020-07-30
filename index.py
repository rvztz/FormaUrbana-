import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
import os

from app import app
from apps import denue, egresos
from navbar import Navbar
nav = Navbar()
app.layout = html.Div([
    nav,
    dcc.Location(id = 'url', refresh = False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input ('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/egresos':
        return egresos.layout
    else:
        return denue.layout

if __name__ == '__main__':
    app.run_server(debug=False)

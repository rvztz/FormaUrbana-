import dash 
from dash_bootstrap_components import themes

app = dash.Dash(__name__, external_stylesheets=[themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.title = 'Forma Urbana Zona Metropolitana Mty'
server = app.server

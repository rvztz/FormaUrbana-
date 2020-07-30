import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input 
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app import app

df_ie = pd.read_csv('/Users/RogerVazquezT/Documents/WorkSpace/EUrb/ingeg.csv')
municipios = ['Abasolo', 'Apodaca', 'Cadereyta', 'El Carmen',
       'Ciénega de Flores', 'García', 'San Pedro', 'General Escobedo',
       'General Zuazua', 'Guadalupe', 'Juárez', 'Monterrey', 'Pesquería',
       'Salinas Victoria', 'San Nicolás', 'Santa Catarina', 'Santiago']

years = ['1990', '2000', '2010', '2015', '2018']

ingresos_options = html.Div([
    html.Div([
        dcc.Dropdown(
            id = 'input-municipio',
            options=[
                {'label': i, 'value': i }
                for i in municipios
            ],
            value = 'Monterrey',
            clearable = False
        )],
        style = {'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id = 'input-years',
            options=[
                {'label': y, 'value': y}
                for y in years
            ],
            value = '2018',
            clearable = False
        )],
        style = {'width': '48%', 'display': 'inline-block'})])

content_ingresos = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                children = [
                    html.H4("Ingresos económicos por municipio", className = "card-title"),
                    html.Hr(),
                    ingresos_options,
                    dcc.Graph(
                        id = "grafica_ingresos" 
                    ),
                    html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eu orci nisi. Nunc et ipsum ligula. Nunc mattis augue purus, efficitur dignissim mi finibus vehicula. In eleifend et tellus et dapibus. Donec ut varius nisl. Donec a libero dui. Proin id gravida leo. Nam vitae justo lorem. Aliquam interdum metus sed nunc fringilla, egestas viverra nisl fringilla. Maecenas facilisis nec quam nec pellentesque. Fusce ultrices egestas libero, a suscipit ex. Donec et tortor libero. Mauris id augue ipsum. Fusce condimentum tristique turpis sed tempor. Sed mattis ex id gravida ultrices.", 
                    className = 'card-text', style = {'text-align':'justify'}),
                    html.P("Duis sollicitudin finibus hendrerit. Cras efficitur lorem nec magna pellentesque consequat. Etiam eget ligula ex. Sed ac ex sed justo pellentesque ornare ac at lectus. Aenean id sollicitudin augue. Integer molestie nibh eu ligula venenatis, eu aliquam risus commodo. Phasellus ac massa quis magna lobortis rutrum ut non lectus. Sed pulvinar nisl sit amet elit laoreet, et placerat diam porta. Curabitur condimentum elementum velit ac efficitur. In hac habitasse platea dictumst. Maecenas ultricies, dui sed lacinia consectetur, arcu lorem lobortis eros, eget scelerisque nisi leo ac felis. Pellentesque erat erat, fringilla id nisl non, efficitur euismod orci. Nulla dolor dolor, scelerisque vitae dignissim condimentum, convallis sit amet nisi.", 
                    className = 'card-text', style = {'text-align':'justify'})
                ],
                className = 'mt-3'
            )
        )
    ]
)

egresos_options = html.Div([
    html.Div([
        dcc.Dropdown(
            id = 'input-municipio',
            options=[
                {'label': i, 'value': i }
                for i in municipios
            ],
            value = 'Monterrey',
            clearable = False
        )],
        style = {'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id = 'input-years',
            options=[
                {'label': y, 'value': y}
                for y in years
            ],
            value = '2018',
            clearable = False
        )],
        style = {'width': '48%', 'display': 'inline-block'})])

content_egresos = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                children = [
                    html.H4("Egresos económicos por municipio", className = "card-title"),
                    html.Hr(),
                    egresos_options,
                    dcc.Graph(
                        id = "grafica_egresos" 
                    ),
                    html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eu orci nisi. Nunc et ipsum ligula. Nunc mattis augue purus, efficitur dignissim mi finibus vehicula. In eleifend et tellus et dapibus. Donec ut varius nisl. Donec a libero dui. Proin id gravida leo. Nam vitae justo lorem. Aliquam interdum metus sed nunc fringilla, egestas viverra nisl fringilla. Maecenas facilisis nec quam nec pellentesque. Fusce ultrices egestas libero, a suscipit ex. Donec et tortor libero. Mauris id augue ipsum. Fusce condimentum tristique turpis sed tempor. Sed mattis ex id gravida ultrices.", 
                    className = 'card-text', style = {'text-align':'justify'}),
                    html.P("Duis sollicitudin finibus hendrerit. Cras efficitur lorem nec magna pellentesque consequat. Etiam eget ligula ex. Sed ac ex sed justo pellentesque ornare ac at lectus. Aenean id sollicitudin augue. Integer molestie nibh eu ligula venenatis, eu aliquam risus commodo. Phasellus ac massa quis magna lobortis rutrum ut non lectus. Sed pulvinar nisl sit amet elit laoreet, et placerat diam porta. Curabitur condimentum elementum velit ac efficitur. In hac habitasse platea dictumst. Maecenas ultricies, dui sed lacinia consectetur, arcu lorem lobortis eros, eget scelerisque nisi leo ac felis. Pellentesque erat erat, fringilla id nisl non, efficitur euismod orci. Nulla dolor dolor, scelerisque vitae dignissim condimentum, convallis sit amet nisi.", 
                    className = 'card-text', style = {'text-align':'justify'})
                ],
                className = 'mt-3'
            )
        )
    ]
)


layout = html.Div(
    children = [
        dbc.Container(
            fluid = True,
            children = [
                html.Div(
                    className = "mt-3 mb-3",
                    children = [
                        html.H2(children = "Ingresos y egresos de municipios de la Zona Metropolitana de Monterrey"),
                        html.Hr()
                    ]),
                
                dbc.Row(
                    children = [
                        dbc.Col(
                            md = 6, 
                            children = [
                                content_ingresos
                            ]
                        ),

                        dbc.Col(
                            md = 6, 
                            children = [
                                content_egresos
                            ]   
                        )
                    ])


            ]
)])
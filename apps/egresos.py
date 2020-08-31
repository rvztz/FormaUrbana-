# -*- coding: UTF-8 -*-
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input 
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from app import app

df_ingeg = pd.read_csv('./data/ingeg.csv')
df_prop = pd.read_csv('./data/propinv.csv')

municipios = df_prop.Municipio.unique()
years = df_prop.Year.unique().astype(str)

color_palette = {'b' :['#16336c' , '#273880' , '#403b8f', '#6a4795' , '#7d508f' , '#8e558a', '#c96971' , '#db6f67' , '#e87e59', '#f7b44a' , '#f5c84e'  , '#eee159', '#e9f864'],
                 'a'  :['#0f2b4f' , '#7d508f', '#e87e59', '#e9f864']}

def get_bubbles(year='2018', hist='a'):
    bubble = px.scatter(df_prop.query('Year=='+year)[df_ingeg['Hist']==hist].dropna(how='any',subset=['prop_inv','prop_ingresos']), x = 'prop_inv', y='prop_ingresos', size='Pob', color = 'Municipio', hover_name='Municipio', template = 'plotly_dark',height=500,size_max=75, 
                    labels = {'prop_inv': 'Gasto en inversión del municipio (per cápita en miles de pesos)', 'prop_ingresos': 'Ingresos propios del municipio (per cápita en miles de pesos)'}, color_discrete_sequence=color_palette[hist])
    return bubble

def get_treeingresos(year='2018',hist='a'):
    tringresos = px.treemap(df_ingeg.query('Year=='+year)[df_ingeg['Hist']==hist].dropna(how='any', subset=['Monto_ingresos', 'Ingresos']), path=['Municipio', 'Ingresos'], values = 'Monto_ingresos', color = 'Monto_ingresos', color_continuous_scale='magma', template = 'plotly_dark',  height=600)
    tringresos.data[0].textinfo = 'label+value+percent parent'
    return tringresos
    

def get_treeegresos(year='2018',hist='a'):
    tregresos = px.treemap(df_ingeg.query('Year=='+year)[df_ingeg['Hist']==hist], path=['Municipio', 'Egresos'], values = 'Monto_egresos', color = 'Monto_egresos', color_continuous_scale='magma', template = 'plotly_dark',  height=600)
    tregresos.data[0].textinfo = 'label+value+percent parent'
    return tregresos

def get_bars(municipio='Monterrey',mode='i'):

    if mode=='i':
        bars = px.line(df_ingeg.query('Municipio=="'+municipio+'"').dropna(subset=['Ingresos', 'Monto_ingresos']), x = 'Year', y = 'Monto_ingresos', color = 'Ingresos',template='plotly_dark', color_discrete_sequence=['#6a4795', '#c96971','#f7b44a'], labels={'Monto_ingresos':'Monto de ingresos (mmdp)', 'Year':'Año'})
    else:
        bars = px.line(df_ingeg.query('Municipio=="'+municipio+'"').dropna(subset=['Egresos', 'Monto_egresos']), x = 'Year', y = 'Monto_egresos', color = 'Egresos',template='plotly_dark', color_discrete_sequence=['#f38d4c', '#a45c85','#59409a', '#f6a04a'], labels={'Monto_egresos':'Monto de ingresos en (mmdp)', 'Year':'Año'})

    bars.update_traces(mode="markers+lines", hovertemplate=None)
    bars.update_layout(hovermode="x unified", height=550, legend=dict(
    orientation= 'h'))
    return bars


main_options = html.Div(children=[

        dcc.Dropdown(
            id = 'input-years',
            options=[
                {'label': y, 'value': y}
                for y in years
            ],
            value = '2018',
            clearable = False,
            style = {
                'backgroundColor': '#121212',
                'color' : '#111111'
            }
        )
        
])

main_options2 = html.Div(children=[

        dcc.Dropdown(
            id = 'input-years2',
            options=[
                {'label': y, 'value': y}
                for y in years
            ],
            value = '2018',
            clearable = False,
            style = {
                'backgroundColor': '#121212',
                'color' : '#111111'
            }
        )
        
])


main_options3 = html.Div(children=[

        dcc.Dropdown(
            id = 'input-years3',
            options=[
                {'label': y, 'value': y}
                for y in years
            ],
            value = '2018',
            clearable = False,
            style = {
                'backgroundColor': '#121212',
                'color' : '#111111'
            }
        )
        
])

main_options4 = html.Div(children=[

        dcc.Dropdown(
            id = 'input-municipio',
            options=[
                {'label': y, 'value': y}
                for y in municipios
            ],
            value = 'Monterrey',
            clearable = False,
            style = {
                'backgroundColor': '#121212',
                'color' : '#111111'
            }
        )
        
])

card_description = dbc.Card([

    dbc.CardHeader('Descripción'),
    dbc.CardBody([
        html.P('El objetivo de esta sección es identificar las fuentes de financiamiento del crecimiento territorial de la mancha urbana (participaciones federales o ingresos propios) y cómo se ha gastado (gasto corriente o inversión). Asimismo, identificar los municipios con el mayor gasto en inversión per cápita. Los municipios de la periferia urbana como García, General Zuazua, Juárez o Cadereyta han tenido un crecimiento habitacional importante en los últimos 15 años, principalmente a través de vivienda social tipo INFONAVIT.'
            ,className = "card-text", style = {'text-align': 'justify', 'font-weight':'bold'}),
        html.P('La pregunta es: ¿en qué medida este desarrollo territorial ha estado financiado a través de participaciones federales versus ingresos propios? La fuente de información para estos comparativos procede de los reportes de Finanzas públicas estatales y municipales de INEGI. Los ingresos y egresos se reportan en cantidades brutas de cada año, sin actualización por la inflación.'
            ,className = "card-text", style = {'text-align': 'justify', 'font-weight':'bold'})

    ])


])

tab_relacion = html.Div(
    children = [
    dbc.Row(
            children = [
                dbc.Col(
                    lg = 6,
                    md = 6,
                    sm = 12,
                    children = [
            html.H3('Relación de ingresos/inversión por municipio', className='card-title', style={'font-weight':'bold'})
                    ]
                ),
                dbc.Col(
                    lg = 6,
                    md = 6, 
                    sm = 12, 
                    align = 'center', 
                    children = [
                        main_options
                    ]
                )
            ]
        ), 
        html.Br(),
        dbc.Row(
            children = [
                dbc.Col(
                    lg = 6,
                    md = 6,
                    sm = 12,
                    children = [
                        html.H6('Municipios históricos', style={'text-align':'center'}),
                        dcc.Graph(
                        id = "grafica_relacion1",
                        figure = get_bubbles(),
                        config = {'displayModeBar':False})]
                ),
                dbc.Col(
                    lg = 6,
                    md = 6, 
                    sm = 12, 
                    children = [
                        html.H6('Municipios de reciente incorporación', style={'text-align':'center'}),
                        dcc.Graph(
                        id = "grafica_relacion2",
                        figure = get_bubbles('2018','b'),
                        config = {'displayModeBar':False})]
    )])]
)

tab_ingresos = html.Div(
    children = [
    dbc.Row(
            children = [
                dbc.Col(
                    lg = 6,
                    md = 6,
                    sm = 12,
                    children = [
            html.H3('Distribución de ingresos por municipio', className='card-title', style={'font-weight':'bold'})
                    ]
                ),
                dbc.Col(
                    lg = 6,
                    md = 6, 
                    sm = 12, 
                    align = 'center', 
                    children = [
                        main_options2
                    ]
                )
            ]
        ), 
        html.Br(),
        dbc.Row(
            children = [
                dbc.Col(
                    lg = 6,
                    md = 6,
                    sm = 12,
                    children = [
                        html.H6('Municipios históricos', style={'text-align':'center'}),
                        dcc.Graph(
                        id = "treemap_ingresos1",
                        figure = get_treeingresos(),
                        config = {'displayModeBar':False})]
                ),
                dbc.Col(
                    lg = 6,
                    md = 6, 
                    sm = 12, 
                    children = [
                        html.H6('Municipios de reciente incorporación', style={'text-align':'center'}),
                        dcc.Graph(
                        id = "treemap_ingresos2",
                        figure = get_treeingresos('2018','b'),
                        config = {'displayModeBar':False})]
    )])]
)

tab_egresos = html.Div(
    children = [
    dbc.Row(
            children = [
                dbc.Col(
                    lg = 6,
                    md = 6,
                    sm = 12,
                    children = [
            html.H3('Distribución de egresos por municipio', className='card-title', style={'font-weight':'bold'})
                    ]
                ),
                dbc.Col(
                    lg = 6,
                    md = 6, 
                    sm = 12, 
                    align = 'center', 
                    children = [
                        main_options3
                    ]
                )
            ]
        ), 
        html.Br(),
        dbc.Row(
            children = [
                dbc.Col(
                    lg = 6,
                    md = 6,
                    sm = 12,
                    children = [
                        html.H6('Municipios históricos', style={'text-align':'center'}),
                        dcc.Graph(
                        id = "treemap_egresos1",
                        figure = get_treeegresos(),
                        config = {'displayModeBar':False})]
                ),
                dbc.Col(
                    lg = 6,
                    md = 6, 
                    sm = 12, 
                    children = [
                        html.H6('Municipios de reciente incorporación', style={'text-align':'center'}),
                        dcc.Graph(
                        id = "treemap_egresos2",
                        figure = get_treeegresos('2018','b'),
                        config = {'displayModeBar':False})]
    )])]
)


content_bars = dbc.Card(
    [
        dbc.CardHeader('Ingresos/egresos'),
        dbc.CardBody([
            dbc.Row(
            children = [
                dbc.Col(
                    lg = 6,
                    md = 6,
                    sm = 12,
                    children = [
            html.H3('Comparativa de ingresos y egresos por municipio 2018 - 1990', className='card-title', style={'font-weight':'bold'})
                    ]
                ),
                dbc.Col(
                    lg = 6,
                    md = 6, 
                    sm = 12, 
                    align = 'center', 
                    children = [
                        main_options4
                    ]
                )
            ]
        ), 
        html.Br(),
        dbc.Row(
            children = [
                dbc.Col(
                    lg = 6,
                    md = 6,
                    sm = 12,
                    children = [
                        html.H6('Ingresos', style={'text-align':'center'}),
                        dcc.Graph(
                        id = "bars_ingresos",
                        figure = get_bars(),
                        config = {'displayModeBar':False})]
                ),
                dbc.Col(
                    lg = 6,
                    md = 6, 
                    sm = 12, 
                    children = [
                        html.H6('Egresos', style={'text-align':'center'}),
                        dcc.Graph(
                        id = "bars_egresos",
                        figure = get_bars('Monterrey','e'),
                        config = {'displayModeBar':False})]
    )])

        ])
    ]
)

distr_tabs = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Rel. Ingresos/Inversión", tab_id="tab-1"),
                    dbc.Tab(label="Distr. Ingresos", tab_id="tab-2"),
                    dbc.Tab(label="Distr. Egresos", tab_id="tab-3")

                ],
                id="distrabs",
                active_tab="tab-1",
            )
        ),
        dbc.CardBody(id="tabcontent"),
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
                        html.H2(children = "Ingresos y egresos de municipios de la Zona Metropolitana de Monterrey", style = {'font-weight':'bold'}),
                        html.Hr()
                    ]),

                dbc.Row(
                    children = [
                        dbc.Col(
                            lg = 12,
                            md = 12,
                            sm = 12,
                            children = [
                                distr_tabs
                            ]
                        )
                    ]),
                    html.Br(),
                    card_description,
                    html.Br(),
                    content_bars
                    ]
)])

@app.callback(Output("tabcontent", "children"), [Input("distrabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab_relacion
    elif at == "tab-2":
        return tab_ingresos
    elif at == "tab-3":
        return tab_egresos
    return html.P("Error al cargar!...")

@app.callback([Output('grafica_relacion1', 'figure'), Output('grafica_relacion2', 'figure')], [Input('input-years','value')])
def select_relacion(selected_year):
    return get_bubbles(selected_year, 'a'), get_bubbles(selected_year, 'b')

@app.callback([Output('treemap_ingresos1', 'figure'), Output('treemap_ingresos2', 'figure')], [Input('input-years2','value')])
def select_relacion2(selected_year2):
    return get_treeingresos(selected_year2, 'a'), get_treeingresos(selected_year2, 'b')

@app.callback([Output('treemap_egresos1', 'figure'), Output('treemap_egresos2', 'figure')], [Input('input-years3','value')])
def select_relacion3(selected_year3):
    return get_treeegresos(selected_year3, 'a'), get_treeegresos(selected_year3, 'b')

@app.callback([Output('bars_ingresos','figure'),Output('bars_egresos','figure')], [Input('input-municipio','value')])
def select_bar(selected_municipio):
    return get_bars(municipio=selected_municipio, mode='i'), get_bars(municipio=selected_municipio, mode='e')

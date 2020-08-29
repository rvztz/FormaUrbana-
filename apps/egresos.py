import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input 
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app import app

df_a = pd.read_csv('./data/ingeng_a.csv')
df_b = pd.read_csv('./data/ingeng_b.csv')
df_prop = pd.read_csv('./data/prop_inv_trans.csv')

municipios = {'Abasolo' :'b', 'Apodaca':'a', 'Cadereyta':'b', 'El Carmen':'b',
       'Ciénaga de Flores':'b', 'García':'b', 'San Pedro':'a', 'General Escobedo':'b',
       'General Zuazua':'b', 'Guadalupe':'a', 'Juárez':'b', 'Monterrey':'a', 'Pesquería':'b',
       'Salinas Victoria':'b', 'San Nicolás':'a', 'Santa Catarina':'b', 'Santiago':'b'}

years = ['1990', '2000', '2010', '2015', '2018']

def get_bubbles(year='2015'):
    bubble = px.scatter(df_prop.query('Año =='+year).dropna(how='any',subset=['prop_inv','prop_ingresos']), x = 'prop_inv', y='prop_ingresos', size='Pob', color = 'Municipio', hover_name='Municipio', template = 'plotly_dark',height=500,size_max=65, labels = {'prop_inv': 'Gasto en inversión del municipio (per cápita en miles de pesos', 'prop_ingresos': 'Ingresos propios del municipio (per cápita en miles de pesos)'})
    return bubble

def get_treeingresos(year='2018',group = 'a'):
    if group=='a':
        df_temp = df_a.query('Año=='+year).dropna(subset=['Monto ingresos', 'Ingresos'])
    elif group == 'b':
        df_temp = df_b.query('Año=='+year).dropna(subset=['Monto ingresos', 'Ingresos'])

    tringresos = px.treemap(df_temp, path=['Municipio', 'Ingresos'], values = 'Monto ingresos', color = 'Monto ingresos', color_continuous_scale='magma', template = 'plotly_dark',  height=700)
    tringresos.data[0].textinfo = 'label+value+percent parent'
    return tringresos
    

def get_treeegresos(year='2018',group = 'a'):
    if group=='a':
        df_temp = df_a.query('Año=='+year).dropna(subset=['Monto egresos', 'Egresos'])
    elif group == 'b':
        df_temp = df_b.query('Año=='+year).dropna(subset=['Monto egresos', 'Egresos'])

    tregresos = px.treemap(df_temp, path=['Municipio', 'Egresos'], values = 'Monto egresos', color = 'Monto egresos', color_continuous_scale='magma', template = 'plotly_dark',  height=700)
    tregresos.data[0].textinfo = 'label+value+percent parent'
    return tregresos

def get_bars(municipio='Monterrey',mode='i'):

    if municipios[municipio]=='a':
        df_temp = df_a.query('Municipio=="'+municipio+'"')
    else:
        df_temp = df_b.query('Municipio=="'+municipio+'"')

    if mode=='i':
        bars = px.line(df_temp.dropna(subset=['Ingresos', 'Monto ingresos']), x = 'Año', y = 'Monto ingresos', color = 'Ingresos',template='plotly_dark')
    else:
        bars = px.line(df_temp.dropna(subset=['Egresos', 'Monto egresos']), x = 'Año', y = 'Monto egresos', color = 'Egresos',template='plotly_dark')
        
    return bars

r_options = html.Div(children=[

    dcc.Dropdown(
            id = 'input-municipio',
            options=[
                {'label': i, 'value': i }
                for i in municipios.keys()
            ],
            value = 'Monterrey',
            clearable = False,
            style = {
                'backgroundColor': '#121212',
                'color' : '#111111'
            }
        )
])

main_options = html.Div(children=[

        dcc.Dropdown(
            id = 'input-years',
            options=[
                {'label': y, 'value': y}
                for y in years
            ],
            value = '2015',
            clearable = False,
            style = {
                'backgroundColor': '#121212',
                'color' : '#111111'
            }
        )
        
])

main_options2 = html.Div(children=[

        html.Div(
        dcc.Dropdown(
            id = 'input-grupo2',
            options=[
                {'label': 'Grupo A', 'value':'a'},
                {'label': 'Grupo B', 'value':'b'},   
            ],
            value = 'a',
            clearable = False,
            style = {
                'backgroundColor': '#121212',
                'color' : '#111111'
            }
        ), 
        style={'width': '48%', 'display': 'inline-block'}
        ),

        html.Div(
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
        ),
    style={'width': '48%', 'float': 'right', 'display': 'inline-block'}
        )
        
])


main_options3 = html.Div(children=[

        html.Div(
        dcc.Dropdown(
            id = 'input-grupo3',
            options=[
                {'label': 'Grupo A', 'value':'a'},
                {'label': 'Grupo B', 'value':'b'},   
            ],
            value = 'a',
            clearable = False,
            style = {
                'backgroundColor': '#121212',
                'color' : '#111111'
            }
        ), 
        style={'width': '48%', 'display': 'inline-block'}
        ),

        html.Div(
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
        ),
    style={'width': '48%', 'float': 'right', 'display': 'inline-block'}
        )
        
])


tab_relacion = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                children = [
                    html.H4("Distribución de ingresos/egresos", className = "card-title"),
                    main_options,
                    dcc.Graph(
                        id = "grafica_relacion",
                        figure = get_bubbles(),
                        config = {
                            'displayModeBar':False
                        }
                    ),
                    html.Br(),
                    html.P('El objetivo de esta sección es identificar las fuentes de financiamiento del crecimiento territorial de la mancha urbana (participaciones federales o ingresos propios) y cómo se ha gastado (gasto corriente o inversión). Asimismo, identificar los municipios con el mayor gasto en inversión per cápita. Los municipios de la periferia urbana como García, General Zuazua, Juárez o Cadereyta han tenido un crecimiento habitacional importante en los últimos 15 años, principalmente a través de vivienda social tipo INFONAVIT.'
            ,className = "card-text", style = {'text-align': 'justify'}),
                    html.P('La pregunta es: ¿en qué medida este desarrollo territorial ha estado financiado a través de participaciones federales versus ingresos propios? La fuente de información para estos comparativos procede de los reportes de Finanzas públicas estatales y municipales de INEGI. Los ingresos y egresos se reportan en cantidades brutas de cada año, sin actualización por la inflación.'
            ,className = "card-text", style = {'text-align': 'justify'})
                ],
                className = 'mt-3'
            )
        )
    ]
)

tab_ingresos = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                children = [
                    html.H4("Distribución ingresos", className = "card-title"),
                    main_options2,
                    dcc.Graph(
                        id = "treemap_ingresos",
                        figure = get_treeingresos(),
                        config = {
                            'displayModeBar':False
                        }
                    )
                ],
                className = 'mt-3'
            )
        )
    ]
)

tab_egresos = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                children = [
                    html.H4("Distribución egresos", className = "card-title"),
                    main_options3,
                    dcc.Graph(
                        id = "treemap_egresos",
                        figure = get_treeegresos(),
                        config = {
                            'displayModeBar': False
                        }
                    )
                ],
                className = 'mt-3'
            )
        )
    ]
)


content_bars = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                children = [
                    html.Br(),
                    html.H4("Ingresos/Egresos económicos por municipio", className = "card-title"),
                    r_options,
                    dcc.Graph(
                        id = "grafica_ingresos" ,
                        figure = get_bars(),
                        config = {
                            'displayModeBar':False
                        }
                    ),
                    html.Br(),
                    dcc.Graph(
                        id = "grafica_egresos",
                        figure = get_bars(mode='e'),
                        config = {
                            'displayModeBar':False
                        }
                    )
                ],
                className = 'mt-3'
            )
        )
    ]
)

distr_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Rel. Ingresos/Egresos", tab_id="tab-1"),
                dbc.Tab(label="Distr. Ingresos", tab_id="tab-2"),
                dbc.Tab(label="Distr. Egresos", tab_id="tab-3")

            ],
            id="distrabs",
            active_tab="tab-1",
        ),
        html.Div(id="tabcontent"),
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
                            lg = 6,
                            md = 6,
                            sm = 12,
                            children = [
                                distr_tabs
                            ]
                        ),

                        dbc.Col(
                             lg = 6,
                            md = 6,
                            sm = 12, 
                            children = [
                                content_bars
                            ]   
                        )
                    ])]
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

@app.callback(Output('grafica_relacion', 'figure'), [Input('input-years','value')])
def select_relacion(selected_year):
    return get_bubbles(selected_year)

@app.callback(Output('treemap_ingresos', 'figure'), [Input('input-grupo2','value'), Input('input-years2','value')])
def select_relacion2(selected_group2, selected_year2):
    return get_treeingresos(selected_year2, selected_group2)

@app.callback(Output('treemap_egresos', 'figure'), [Input('input-grupo3','value'), Input('input-years3','value')])
def select_relacion3(selected_group3, selected_year3):
    return get_treeegresos(selected_year3, selected_group3)

@app.callback([Output('grafica_ingresos','figure'),Output('grafica_egresos','figure')], [Input('input-municipio','value')])
def select_bar(selected_municipio):
    return get_bars(municipio=selected_municipio, mode='i'), get_bars(municipio=selected_municipio, mode='e')

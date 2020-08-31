import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input 
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from app import app

df_censo = pd.read_csv('./data/censo.csv')
df_concen = pd.read_csv("./data/gradiente.csv")
df_denue = pd.read_csv('./data/denue.csv')
radio = json.load(open('./data/MapaGradientes.json'))


empleos_content = { 
    '2010_1' : 'En el año 2010 el comercio fue la principal fuente de empleos en el Área Metropolitana de Monterrey, representando el 35.9% de los empleos totales, siendo la industria el segundo principal empleador con el 23.4% del total. Entre los 3 y 7 kilómetros de distancia del centro se aglomera el 35% de los empleos totales, el comercial representando el 35.6% de ellos. Esta alta concentración de empleos delimita una zona funcional bastante monocéntrica que abarca principalmente las zonas de Valle Oriente, Centro de San Pedro Garza García y el Tecnológico de Monterrey. Es de notar que la concentración de empleos no ocurre en el propio centro histórico de la ciudad, teniendo los primeros dos kilómetros a la redonda de la Macroplaza sólo el 10% de los empleos totales.',
    '2010_2' : 'Adicionalmente, se puede observar una menor concentración de empleos entre los 11 y 14 kilómetros de distancia, que corresponden a zonas de Guadalupe, San Nicolás de los Garza, Santa Catarina y Cumbres. El 19% de los empleos del área metropolitana se concentran aquí, siendo el comercio el 38.7% y la industria el 25% de los empleos del sector. Esta concentración puede indicar el desarrollo de nuevos centros y marca la tendencia hacia mayor policentrismo en la ciudad. De igual forma existe una leve concentración de empleos entre 31 y 34 kilómetros de distancia, que corresponde a los núcleos de García, Cadereyta Jiménez, Santiago y Salinas Victoria. Aunque estos sectores contienen sólo el 2.3% de los empleos de 2010, se puede observar un incremento a comparación de distancias un poco anteriores.',
    '2015_1' : 'Al año 2015 se nota un considerable incremento en los empleos del sector de oficinas y servicios dentro del núcleo establecido entre los 3 y 7 kilómetros de distancia, con los trabajos de oficina incluso superando aquellos de industria, ahora cada uno representando el 21.8% y 18.3% respectivamente. En 2010 estos dos juntos representaban el 27.5% del sector e incrementaron a representar el 32% del total de la zona. A los 12, 22 y 33 kilómetros de distancia, correspondiendo principalmente a las zonas de Guadalupe, San Nicolás de los Garza, Santa Catarina, Cumbres, Juárez y García, sucedió otro considerable incremento en empleos, particularmente en los ámbitos comerciales e industriales, con incrementos totales del 11.7%, 66% y 25.2% respectivamente.',
    '2015_2' : 'Esto marca una tendencia a la consolidación del centro, particularmente en los sectores terciarios, así como el continuo crecimiento de otros núcleos a mayor distancia. La productividad de estos nuevos centros de empleos dependerá de la accesibilidad a ellos por parte de la población y la facilidad de movilidad en la ciudad. Es posible que los viajes entre subnúcleos se vuelvan cada vez más relevantes, sin la necesidad de pasar por el núcleo previamente consolidado. El centro histórico sufrió incluso una pérdida de empleos del 10%.',
    '2019_1' : 'Al 2019 el centro consolidado entre los 3 y 7 kilómetros de distancia vio un fuerte desarrollo de empleos. Esta zona correspondiente principalmente a San Pedro Garza García y al Tecnológico de Monterrey vio un crecimiento del 11%, sin embargo, ha perdido relevancia en cuanto a concentración de empleos. En este año concentró el 31.8% de los empleos del área metropolitana, a comparación del 35% y 33% que concentraba en el año 2010 y 2015 respectivamente. Al año 2019 se mantienen las tendencias de crecimiento que se observaron en el 2015. Se nota una fuerte consolidación de empleos a 12 kilómetros, coincidiendo con las zonas de Cumbres, Santa Catarina, San Nicolás de los Garza y Guadalupe, con un aumento del 18.5%, correspondiente a más de 12,000 empleos. En el centro previamente consolidado a 6 kilómetros existe de igual forma un fuerte incremento en empleos de comercio y de oficina, habiendo aumentado por 16% y 28% respectivamente a comparación del 2015. La industria cobró mayor importancia entre los 19 y 22 kilómetros del centro, correspondiente a Santa Catarina, Mitras, Juárez, Escobedo y Apodaca. Se vio un incremento del 34% respecto a 2015 y representó el 47% de los empleos totales. La tendencia de empleos muestra un incremento en centros de empleabilidad a lo largo de la zona metropolitana y una disminución en la dependencia del centro histórico de la ciudad.',
    '2019_2' : 'En el aspecto global del área metropolitana, los empleos totales incrementaron por el 14%, siendo los empleos de oficina el sector con mayor crecimiento, del 20.7% respecto a 2015. La industria y el comercio tuvieron un crecimiento cercano, del 19.7% y 19.6% respectivamente. Sin embargo, el comercio sigue siendo la principal fuente de empleo del área metropolitana, representando el 36% de los empleos totales. La industria representó el 23% y los empleos de oficina y servicios representaron el 15% y 10% respectivamente.',
    'censo_1': 'En cuanto a población se nota una marcada tendencia entre 2000 y 2016. Los primeros 11 kilómetros de la ciudad han sido despoblados marcadamente, con una pérdida del 12% de la población respecto al año 2000, este sector de la ciudad comprende el centro histórico y se extiende hasta San Pedro Garza García, el inicio de Carretera Nacional, el centro de Guadalupe, el centro de San Nicolás de los Garza y Mitras Centro. Sin embargo, el número de viviendas en este sector incrementó en 11.7%, indicando que, aunque la población está deshabitando la zona, la construcción continúa, probablemente provocando una caída en la densidad de población de la mancha urbana.',
    'censo_2': 'No obstante, la población total de la ciudad ha incrementado en 22%, pasando de 3,3332,000 habitantes en el año 2000 a 4,062,800 en el 2016. Esto significa que la población se ha ido a las periferias de la ciudad, más allá de los primeros 11 kilómetros, teniendo el kilómetro 15 un aumento de más de 100 mil habitantes. El incremento de población entre los 12 kilómetros y los 40 ha sido del 66%. De igual forma a estas distancias el número de viviendas a incrementado considerablemente, pasando de 340,209 viviendas en el 2000 a 896,873 en el año 2016, es decir, un incremento de más del 160% por ciento. Esto demuestra una mayor demanda habitacional en las periferias de la ciudad. Mientras que en el año 2000 sólo el 43.5% de la población vivía a más de 11 kilómetros del centro histórico, en el 2016 fue el 59.1% quién habitó las periferias del área metropolitana. Este cambio de zonas de habitación significa mayores distancias de traslado al centro de empleos consolidado históricamente. Sin embargo, también suponen nuevas fuentes de empleo en servicios y comercios para satisfacer las necesidades de los nuevos habitantes.'
}

maps_titles = {
    'dist_cbd': 'Distancia al centro de la ciudad',
    'Pop0_16' : 'Diferencia de población/empleo 2016 - 2000',
    'CUS': 'Coeficiente de uso de suelo (CUS)', 
    'PPJov2016':'Porcentaje de población menor a quince años',
    'act_econ':'Actividades económicas',
    'pob_viv':'Poblacion y vivienda 2016 - 2000'
}

maps_contents = {
    'dist_cbd' : ['Esta sección realiza una exploración del cambio de la función urbana de monterrey considerando los cambios en la morfología policéntrica de la ciudad ocurridos en los últimos veinte y treinta años. En este análisis, se trazaron círculos concéntricos de 1 kilómetro a partir de la macroplaza hasta los 40 kilómetros de distancia del centro de la ciudad. Los círculos fueron cortados con el tamaño de la mancha urbana actual para generar una serie de métricas que exploran el cambio en la ubicación de viviendas y empleos en el período comprendido entre el 2000 y el 2020.', ''],
    'Pop0_16':['Esta serie de mapas fueron construidos a partir de información disponible en INEGI. En el caso poblacional, se utilizó la cartografía de manzanas del Censo del año 2000 y del Inventario Nacional de Viviendas del 2016. En el caso del empleo, se utilizó el Directorio Estadístico Nacional de Unidades Económicas (DENUE) del año 2000 y del 2019. Los colores oscuros del mapa de diferencia de población indican las zonas que perdieron población entre el 2000 y el 2016; los colores claros identifican las zonas que aumentaron población.', 
    'En el caso del empleo, se puede apreciar una pérdida de empleos en el centro de la ciudad y en el periurbano, pero un incremento en los círculos ubicados entre 12 y 19 kilómetros de distancia del centro de la ciudad. Estos mapas muestran que en los últimos quince años ha ocurrido una migración residencial del centro de la ciudad hacia la periferia. Los empleos también han migrado hacia zonas no centrales, consolidando una morfología policéntrica de la ZMM.'],
    'CUS': ['A partir de la información catastral consultada, estimamos el Coeficiente de Utilización del Suelo (CUS) promedio en los círculos concéntricos trazados a partir del centro de la ciudad. Los colores más claros indican una mayor proporción de área construida contra área del terreno. La zona central de la ciudad tiene el CUS más alto, el cual se reduce gradualmente conforme nos movemos del centro hacia la periferia. La excepción son algunas franjas claras ubicadas en García y Juárez, con un CUS muy alto y que corresponden a desarrollos de vivienda social.', ''],
    'PPJov2016':['Esta serie de mapas identifican los hogares jóvenes a partir de la información de INEGI de los años 1990, 2000, 2010 y del Inventario Nacional de Vivienda del 2016. En los censos nacionales se pregunta por el número de personas por hogar que son menores de 15 años. Dicha variable es un aproximado para identificar la ubicación residencial de aquellos hogares que se formaron en un periodo menor a los últimos 15 años.',
    'Observando los mapas de 1990, 2000 y 2016, encontramos que los hogares jóvenes no se ubican en las zonas centrales de la ciudad, sino en zonas consolidadas en la periferia urbana. Esto parece ser un indicador de la incapacidad de regeneración del suelo en la zona central de la ciudad para generar una oferta de vivienda asequible a las necesidades de los nuevos hogares. Pareciera que la oferta de vivienda para los nuevos hogares se concentra recurrentemente (al menos desde 1990) en el limite urbano en su momento.']
}

def get_denue(year='2019'):
    if year==None:
        year = '2019'
    
    fig_denue = go.Figure()
    
    fig_denue.add_trace(go.Scatter(x=df_denue.query('anno=='+year)['dist_cbd'], y=df_denue.query('anno=='+year)['comercio'],
            name='Comercio', line=dict(color = '#403b8f', width =3)))

    fig_denue.add_trace(go.Scatter(x=df_denue.query('anno=='+year)['dist_cbd'], y=df_denue.query('anno=='+year)['industria'],
            name='Industria', line=dict(color = '#a45c85', width =3)))

    fig_denue.add_trace(go.Scatter(x=df_denue.query('anno=='+year)['dist_cbd'], y=df_denue.query('anno=='+year)['oficina'],
            name='Oficina', line=dict(color = '#f38d4c', width =3)))

    fig_denue.add_trace(go.Scatter(x=df_denue.query('anno=='+year)['dist_cbd'], y=df_denue.query('anno=='+year)['servicios'],
            name='Servicios', line=dict(color = '#e9f864', width =3)))

    fig_denue.update_traces(
        mode='lines+markers',
        hovertemplate = None
    )
    
    fig_denue.update_layout(
    hovermode="x unified", 
    xaxis_title="Distancia a centro de la ciudad (km)",
    yaxis_title="Número de empleos",
    template= 'plotly_dark',
    height=500
    )

    return fig_denue

def get_censo():
    fig_censo = go.Figure()

    fig_censo.add_trace(go.Scatter(x=df_censo.query('year==2000')['dist_cbd'], y=df_censo.query('year==2000')['viv_cm'],
                    name='Vivienda 2000', line = dict(color='#7d508f',width=3)))

    fig_censo.add_trace(go.Scatter(x=df_censo.query('year==2000')['dist_cbd'], y=df_censo.query('year==2000')['pop_cm'],
                    name='Población 2000', line = dict(color='#f5c84e',width=3)))

    fig_censo.add_trace(go.Scatter(x=df_censo.query('year==2016')['dist_cbd'], y=df_censo.query('year==2016')['viv_cm'],
                    name='Vivienda 2016', line = dict(color='#a45c85',width=3)))

    fig_censo.add_trace(go.Scatter(x=df_censo.query('year==2016')['dist_cbd'], y=df_censo.query('year==2016')['pop_cm'],
                    name='Población 2016', line = dict(color='#e9f864',width=3)))

    fig_censo.update_traces(
        mode='lines+markers',
        hovertemplate=None
    )

    fig_censo.update_layout(
        hovermode='x unified',
        xaxis_title="Distancia a centro de la ciudad (km)",
        yaxis_title="Número de personas",
        template = 'plotly_dark',
        height=500
    )

    return fig_censo

def get_mapa(row="dist_cbd"):
    if row==None:
        row = "dist_cbd"
    distance = px.choropleth_mapbox(df_concen, geojson = radio, color = row,locations = "dist_cbd",color_continuous_scale='Magma_r' ,featureidkey= "properties.distance", center = {"lat": 25.668289, "lon": -100.310015}, mapbox_style='carto-darkmatter', zoom=8.5, height=550, labels = {'dist_cbd': 'Distancia', 'Emp10_19' : 'Empleo', 'Pop0_16': 'Población'})
    distance.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, template = 'plotly_dark')
    return distance


denue_options = dcc.Dropdown(
    options=[
        {'label': 'Actividades económicas 2010', 'value': '2010'},
        {'label': 'Actividades económicas 2015', 'value': '2015'},
        {'label': 'Actividades económicas 2019', 'value': '2019'},
    ],
    id = "denue-options",
    value='2019',
    clearable=False,
    style = {
        'backgroundColor': '#121212',
        'color' : '#111111'
    }
)  

pob_options= dcc.Dropdown(
    options=[
        {'label': 'Diferencia de población', 'value': 'Pop0_16'},
        {'label': 'Diferencia de empleo', 'value': 'Emp10_19'},
    ],
    id = "pob-options",
    value='Pop0_16',
    clearable=False,
    style = {
        'backgroundColor': '#121212',
        'color' : '#111111'
    }
)  

suelo_options= dcc.Dropdown(
    options=[
        {'label': 'Coef. uso de suelo', 'value': 'CUS'},
        {'label': 'Área construida', 'value': 'AreaC'},
        {'label': 'Proporción pavimentos-construcción', 'value': 'PropPC'},
        {'label': 'Consumo per cápita de pavimentos', 'value': 'ConpP'},
        {'label': 'Porcentaje área pavimentada', 'value': 'PorPav'}
    ],
    id = "suelo-options",
    value='CUS',
    clearable=False,
    style = {
        'backgroundColor': '#121212',
        'color' : '#111111'
    }
)  

jov_options = dcc.Dropdown(
    options=[
        {'label': 'Población menor a quince años - 1990', 'value': 'PPJov90'},
        {'label': 'Población menor a quince años - 2000', 'value': 'PPJov2000'},
        {'label': 'Población menor a quince años - 2016', 'value': 'PPJov2016'},
        {'label': 'Cambio de población menor a quince años 2016-1990', 'value': 'CambioPP90'}

    ],
    id = "jov-options",
    value='PPJov2016',
    clearable=False,
    style = {
        'backgroundColor': '#121212',
        'color' : '#111111'
    }
)  


tab_denue = html.Div(
        children = [
            denue_options,
            dcc.Graph(
                figure = get_denue(),
                id = "grafica_denue",
                config = {
                    'displayModeBar' : False
                }
            )
        ]
)   

tab_censo = html.Div(
        children = [
            dcc.Graph(
                figure = get_censo(),
                config = {
                    'displayModeBar' : False
                }
            )
        ]
)   



map_distancia = html.Div(
        children = [
            dcc.Graph(
                figure = get_mapa('dist_cbd'),
                config = {
                    'displayModeBar' : False
                }
            )
        ]
)

map_poblacion = html.Div(
        children = [
            pob_options,
            dcc.Graph(
                id = 'map_pobemp',
                figure = get_mapa('Pop0_16'),
                config = {
                    'displayModeBar' : False
                }
            )
        ]
)   

map_cus = html.Div(
        children = [
            suelo_options,
            dcc.Graph(
                id = 'map_uso',
                figure = get_mapa('CUS'),
                config = {
                    'displayModeBar' : False
                }
            )
        ]
    )   


map_joven = html.Div(
        children = [
            jov_options,
            dcc.Graph(
                id = 'map_joven',
                figure = get_mapa('PPJov2000'),
                config = {
                    'displayModeBar' : False
                }
            )
        ]
)   


map_tabs = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Dist. centro", tab_id="maptab-1"),
                    dbc.Tab(label="Población/empleo", tab_id="maptab-2"),
                    dbc.Tab(label="Uso suelo", tab_id="maptab-3"),
                    dbc.Tab(label="Pob. joven", tab_id="maptab-4")

                ],
                id="maptabs",
                active_tab="maptab-1",
            )
        ),
        html.Div(id="mapcontent")
    ]
)

tabs = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Act. Económicas", tab_id="tab-1"),
                    dbc.Tab(label="Población y vivienda", tab_id="tab-2")

                ],
                id="tabs",
                active_tab="tab-1",
            )
        ),
        html.Div(id="content"),
    ]
)


map_card = dbc.Card(
    [
        dbc.CardHeader("Función urbana"),
        dbc.CardBody(
            [
                html.H3(children =maps_titles['dist_cbd'], className="card-title", style={'font-weight':'bold'}, id='maptitle'),
                html.P(maps_contents['dist_cbd'][0], className="card-text", style = {'text-align': 'justify'}, id='mapc_1'),
                html.P(maps_contents['dist_cbd'][1], className="card-text", style = {'text-align': 'justify'}, id='mapc_2')
            ]
        )
    ],
)

graph_card = dbc.Card(
    [
        dbc.CardHeader("Empleos y población"),
        dbc.CardBody(
            [
                html.H3(children =maps_titles['act_econ'], className="card-title", style={'font-weight':'bold'}, id='gratitle'),
                html.P(empleos_content['2019_1'], className="card-text", style = {'text-align': 'justify'}, id='grac_1'),
                html.P(empleos_content['2019_1'], className="card-text", style = {'text-align': 'justify'}, id='grac_2')
            ]
        )
    ],
)

layout = html.Div(
    children = [
    dbc.Container(
        fluid=True,
        children=[
        html.Div(
            className = "mt-3 mb-3",
            children =[
            html.H2(children ="Función urbana de la Zona Metropolitana de Monterrey", style = {'font-weight':'bold'}),
            html.Hr()
            ]), 
        dbc.Row(
            children = [
                dbc.Col(
                    lg = 7,
                    md = 7,
                    sm = 12,
                    children = [
                        map_tabs
                    ]
                ),
                dbc.Col(
                    lg = 5,
                    md = 5, 
                    sm = 12, 
                    align = 'center', 
                    children = [
                        map_card
                    ]
                )
            ]
        ),
        html.Br(), 
        dbc.Row(
            children = [
                dbc.Col(
                    lg = 7,
                    md = 7,
                    sm = 12,
                    children = [
                        tabs
                    ]
                ),
                dbc.Col(
                    lg = 5,
                    md = 5, 
                    sm = 12, 
                    align ='center',
                    children = [
                        graph_card
                    ]
                )
            ]
        )        
        ])
    

])

@app.callback([Output("content", "children"), Output("gratitle", "children"), Output("grac_1", "children"), Output("grac_2", "children")], [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab_denue, maps_titles['act_econ'], empleos_content['2019_1'], empleos_content['2019_2']
    elif at == "tab-2":
        return tab_censo, maps_titles['pob_viv'], empleos_content['censo_1'], empleos_content['censo_2']
    return html.P("Error al cargar!...")

@app.callback([Output("mapcontent", "children"), Output("maptitle", "children"), Output("mapc_1", "children"), Output("mapc_2", "children")], [Input("maptabs", "active_tab")])
def switch_maptab(at):
    if at == "maptab-1":
        return map_distancia, maps_titles['dist_cbd'], maps_contents['dist_cbd'][0], maps_contents['dist_cbd'][1]
    elif at == "maptab-2":
        return map_poblacion, maps_titles['Pop0_16'], maps_contents['Pop0_16'][0], maps_contents['Pop0_16'][1]
    elif at == "maptab-3":
        return map_cus, maps_titles['CUS'], maps_contents['CUS'][0], maps_contents['CUS'][1]
    elif at == "maptab-4":
        return map_joven, maps_titles['PPJov2016'], maps_contents['PPJov2016'][0], maps_contents['PPJov2016'][1]
    return html.P("Error al cargar!...")


@app.callback(Output("grafica_denue", "figure"), [Input("denue-options", "value")])
def select_figure(selected_year):
    return get_denue(selected_year)

@app.callback(Output('map_pobemp','figure'), [Input('pob-options','value')])
def select_pob1(selected_cat1):
        return get_mapa(selected_cat1)

@app.callback(Output('map_uso','figure'), [Input('suelo-options','value')])
def select_pob2(selected_cat2):
        return get_mapa(selected_cat2)

@app.callback(Output('map_joven','figure'), [Input('jov-options','value')])
def select_pob3(selected_cat3):
        return get_mapa(selected_cat3)
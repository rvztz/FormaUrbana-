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
    '2019_2' : 'En el aspecto global del área metropolitana, los empleos totales incrementaron por el 14%, siendo los empleos de oficina el sector con mayor crecimiento, del 20.7% respecto a 2015. La industria y el comercio tuvieron un crecimiento cercano, del 19.7% y 19.6% respectivamente. Sin embargo, el comercio sigue siendo la principal fuente de empleo del área metropolitana, representando el 36% de los empleos totales. La industria representó el 23% y los empleos de oficina y servicios representaron el 15% y 10% respectivamente.'
}

maps_titles = {
    'Pop0_16' : 'Diferencia de población 2000 - 2016',
    'Emp10_19' : 'Diferencia de empleos 2010 - 2019',
    'CUS': 'Coeficiente de uso de suelo', 
    'AreaC':'Metros cuadrados de área construida',
    'PPJov2000':'Población joven 2000',
    'PPJov2016':'Población joven 2016',
    'CambioPP':'Diferencia de población joven 2000 - 2016',
    'PropPC':'Proporción pavimentos-construcción',
    'ConpP':'Consumo per cápita de paviementos',
    'AreaPav':'Área pavimentada'
}

def get_denue(year='2019'):
    if year==None:
        year = '2019'
    
    fig_denue = go.Figure()
    
    fig_denue.add_trace(go.Scatter(x=df_denue.query('anno=='+year)['dist_cbd'], y=df_denue.query('anno=='+year)['comercio'],
            mode='lines+markers',
            name='Comercio'))

    fig_denue.add_trace(go.Scatter(x=df_denue.query('anno=='+year)['dist_cbd'], y=df_denue.query('anno=='+year)['industria'],
            mode='lines+markers',
            name='Industria'))

    fig_denue.add_trace(go.Scatter(x=df_denue.query('anno=='+year)['dist_cbd'], y=df_denue.query('anno=='+year)['oficina'],
            mode='lines+markers',
            name='Oficina'))

    fig_denue.add_trace(go.Scatter(x=df_denue.query('anno=='+year)['dist_cbd'], y=df_denue.query('anno=='+year)['servicios'],
            mode='lines+markers',
            name='Servicios'))
    

    fig_denue.update_layout(
    xaxis_title="Distancia a centro de la ciudad",
    yaxis_title="Número de trabajos",
    template= 'plotly_dark'
    )

    return fig_denue

def get_censo():
    fig_censo = go.Figure()

    fig_censo.add_trace(go.Scatter(x=df_censo.query('year==2000')['dist_cbd'], y=df_censo.query('year==2000')['viv_cm'],
                    mode='lines',
                    name='Vivienda 2000'))

    fig_censo.add_trace(go.Scatter(x=df_censo.query('year==2000')['dist_cbd'], y=df_censo.query('year==2000')['pop_cm'],
                    mode='lines',
                    name='Población 2000'))

    fig_censo.add_trace(go.Scatter(x=df_censo.query('year==2016')['dist_cbd'], y=df_censo.query('year==2016')['viv_cm'],
                    mode='lines',
                    name='Vivienda 2016'))

    fig_censo.add_trace(go.Scatter(x=df_censo.query('year==2016')['dist_cbd'], y=df_censo.query('year==2016')['pop_cm'],
                    mode='lines',
                    name='Población 2016'))

    fig_censo.update_layout(
        xaxis_title="Distancia a centro de la ciudad",
        yaxis_title="Número de personas",
        template = 'plotly_dark'
    )

    return fig_censo

def get_mapa(row="dist_cbd"):
    if row==None:
        row = "dist_cbd"
    distance = px.choropleth_mapbox(df_concen, geojson = radio, color = row,locations = "dist_cbd",color_continuous_scale='Magma' ,featureidkey= "properties.distance", center = {"lat": 25.668289, "lon": -100.310015}, mapbox_style='carto-darkmatter', zoom=8.5, height=550, labels = {'dist_cbd': 'Distancia', 'Emp10_19' : 'Empleo', 'Pop0_16': 'Población'})
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
        {'label': 'Consumo per cápita de pavimientos', 'value': 'ConpP'},
        {'label': 'Área pavimentada', 'value': 'AreaPav'}
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
        {'label': 'Población joven 2000', 'value': 'PPJov2000'},
        {'label': 'Población joven 2016', 'value': 'PPJov2016'},
        {'label': 'Cambio de población joven', 'value': 'CambioPP'}

    ],
    id = "jov-options",
    value='PPJov2000',
    clearable=False,
    style = {
        'backgroundColor': '#121212',
        'color' : '#111111'
    }
)  


tab_denue = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4("Actividades Económicas", className = "card-title"),
            denue_options,
            html.Br(),
            dcc.Graph(
                figure = get_denue(),
                id = "grafica_denue",
                config = {
                    'displayModeBar' : False
                }
            ),
            html.Br(),
            html.P(children = empleos_content['2019_1']
            ,className = "card-text", style = {'text-align': 'justify'}, id = 'p_act1'),
            html.P(children = empleos_content['2019_2']
            , className = "card-text", style = {'text-align': 'justify'}, id = 'p_act2')

        ],
        className = "mt-3"
    )   
)

tab_censo = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4("Población y vivienda 2000/2016", className = "card-title"),
            html.Hr(),
            html.P("En cuanto a población se nota una marcada tendencia entre 2000 y 2016. Los primeros 11 kilómetros de la ciudad han sido despoblados marcadamente, con una pérdida del 12% de la población respecto al año 2000, este sector de la ciudad comprende el centro histórico y se extiende hasta San Pedro Garza García, el inicio de Carretera Nacional, el centro de Guadalupe, el centro de San Nicolás de los Garza y Mitras Centro. Sin embargo, el número de viviendas en este sector incrementó en 11.7%, indicando que, aunque la población está deshabitando la zona, la construcción continúa, probablemente provocando una caída en la densidad de población de la mancha urbana."
            ,className = "card-text", style = {'text-align': 'justify'}),
            html.P("No obstante, la población total de la ciudad ha incrementado en 22%, pasando de 3,3332,000 habitantes en el año 2000 a 4,062,800 en el 2016. Esto significa que la población se ha ido a las periferias de la ciudad, más allá de los primeros 11 kilómetros, teniendo el kilómetro 15 un aumento de más de 100 mil habitantes. El incremento de población entre los 12 kilómetros y los 40 ha sido del 66%. De igual forma a estas distancias el número de viviendas a incrementado considerablemente, pasando de 340,209 viviendas en el 2000 a 896,873 en el año 2016, es decir, un incremento de más del 160% por ciento. Esto demuestra una mayor demanda habitacional en las periferias de la ciudad. Mientras que en el año 2000 sólo el 43.5% de la población vivía a más de 11 kilómetros del centro histórico, en el 2016 fue el 59.1% quién habitó las periferias del área metropolitana."
            ,className = "card-text", style = {'text-align': 'justify'}),
            html.P("Este cambio de zonas de habitación significa mayores distancias de traslado al centro de empleos consolidado históricamente. Sin embargo, también suponen nuevas fuentes de empleo en servicios y comercios para satisfacer las necesidades de los nuevos habitantes."
            ,className = "card-text", style = {'text-align': 'justify'}),
            dcc.Graph(
                figure = get_censo(),
                config = {
                    'displayModeBar' : False
                }
            )
        ],
        className = "mt-3"
    )   
)

map_distancia = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4("Distancia al centro de la ciudad", className = "card-title"),
            dcc.Graph(
                figure = get_mapa('dist_cbd'),
                config = {
                    'displayModeBar' : False
                }
            )
        ],
        className = "mt-3"
    )   
)

map_poblacion = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4(children=maps_titles['Pop0_16'], className = "card-title", id='titulopob'),
            pob_options,
            dcc.Graph(
                id = 'map_pobemp',
                figure = get_mapa('Pop0_16'),
                config = {
                    'displayModeBar' : False
                }
            )
        ],
        className = "mt-3"
    )   
)

map_cus = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4(children=maps_titles['CUS'], className = "card-title", id ='titulo_suelo'),
            suelo_options,
            dcc.Graph(
                id = 'map_uso',
                figure = get_mapa('CUS'),
                config = {
                    'displayModeBar' : False
                }
            )
        ],
        className = "mt-3"
    )   
)


map_joven = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4(children=maps_titles['PPJov2000'], className = "card-title", id='titulo_joven'),
            jov_options,
            dcc.Graph(
                id = 'map_joven',
                figure = get_mapa('PPJov2000'),
                config = {
                    'displayModeBar' : False
                }
            )
        ],
        className = "mt-3"
    )   
)


map_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Dist. centro", tab_id="maptab-1"),
                dbc.Tab(label="Población/empleo", tab_id="maptab-2"),
                dbc.Tab(label="Uso suelo", tab_id="maptab-3"),
                dbc.Tab(label="Población joven", tab_id="maptab-4")

            ],
            id="maptabs",
            active_tab="maptab-1",
        ),
        html.Div(id="mapcontent"),
    ]
)

tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Act. Economicas", tab_id="tab-1"),
                dbc.Tab(label="Población y vivienda", tab_id="tab-2")

            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div(id="content"),
    ]
)

layout = html.Div(
    children = [
    dbc.Container(
        fluid=True,
        children=[
        html.Div(
            className = "mt-3 mb-3",
            children =[
            html.H2(children ="Forma urbana de la Zona Metropolitana de Monterrey"),
            html.Hr()
            ]), 
        dbc.Row(
            children = [
                dbc.Col(
                    lg = 6,
                    md = 6,
                    sm = 12,
                    children = [
                        tabs
                    ]
                ),
                dbc.Col(
                    lg = 6,
                    md = 6, 
                    sm = 12, 
                    children = [
                        map_tabs
                    ]
                )


            ]
        )])
    

])

@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab_denue
    elif at == "tab-2":
        return tab_censo
    return html.P("Error al cargar!...")

@app.callback(Output("mapcontent", "children"), [Input("maptabs", "active_tab")])
def switch_maptab(at):
    if at == "maptab-1":
        return map_distancia
    elif at == "maptab-2":
        return map_poblacion
    elif at == "maptab-3":
        return map_cus
    elif at == "maptab-4":
        return map_joven
    return html.P("Error al cargar!...")

@app.callback([Output("grafica_denue", "figure"), Output("p_act1", "children"), Output("p_act2", "children")], [Input("denue-options", "value")])
def select_figure(selected_year):
    return get_denue(selected_year), empleos_content[selected_year+'_1'], empleos_content[selected_year+'_2']

@app.callback([Output('map_pobemp','figure'), Output('titulopob', 'children')], [Input('pob-options','value')])
def select_pob1(selected_cat1):
        return get_mapa(selected_cat1), maps_titles[selected_cat1]

@app.callback([Output('map_uso','figure'), Output('titulo_suelo', 'children')], [Input('suelo-options','value')])
def select_pob2(selected_cat2):
        return get_mapa(selected_cat2), maps_titles[selected_cat2]

@app.callback([Output('map_joven','figure'), Output('titulo_joven', 'children')], [Input('jov-options','value')])
def select_pob3(selected_cat3):
        return get_mapa(selected_cat3), maps_titles[selected_cat3]
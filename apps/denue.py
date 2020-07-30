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

df_censo = pd.read_csv('~/Documents/Workspace/EUrb/CensoMTY2000_10_16CBD.csv')
df_concen = pd.read_csv("~/Documents/WorkSpace/EUrb/GradientesPop_Jobs.csv")
df_denue = pd.read_csv('~/Documents/WorkSpace/EUrb/DENUEMTYCBD_2010_15_19.csv')
available_denue = ['comercio','industria', 'oficina', 'servicios'] 
radio = json.load(open('/Users/RogerVazquezT/Documents/WorkSpace/EUrb/MapaGradientes.json'))


empleos_content = { 
    '2010_1' : 'En el año 2010 el comercio fue la principal fuente de empleos en el Área Metropolitana de Monterrey, representando el 35.9% de los empleos totales, siendo la industria el segundo principal empleador con el 23.4% del total. Entre los 3 y 7 kilómetros de distancia del centro se aglomera el 35% de los empleos totales, el comercial representando el 35.6% de ellos. Esta alta concentración de empleos delimita una zona funcional bastante monocéntrica que abarca principalmente las zonas de Valle Oriente, Centro de San Pedro Garza García y el Tecnológico de Monterrey. Es de notar que la concentración de empleos no ocurre en el propio centro histórico de la ciudad, teniendo los primeros dos kilómetros a la redonda de la Macroplaza sólo el 10% de los empleos totales.',
    '2010_2' : 'Adicionalmente, se puede observar una menor concentración de empleos entre los 11 y 14 kilómetros de distancia, que corresponden a zonas de Guadalupe, San Nicolás de los Garza, Santa Catarina y Cumbres. El 19% de los empleos del área metropolitana se concentran aquí, siendo el comercio el 38.7% y la industria el 25% de los empleos del sector. Esta concentración puede indicar el desarrollo de nuevos centros y marca la tendencia hacia mayor policentrismo en la ciudad. De igual forma existe una leve concentración de empleos entre 31 y 34 kilómetros de distancia, que corresponde a los núcleos de García, Cadereyta Jiménez, Santiago y Salinas Victoria. Aunque estos sectores contienen sólo el 2.3% de los empleos de 2010, se puede observar un incremento a comparación de distancias un poco anteriores.',
    '2015_1' : 'Al año 2015 se nota un considerable incremento en los empleos del sector de oficinas y servicios dentro del núcleo establecido entre los 3 y 7 kilómetros de distancia, con los trabajos de oficina incluso superando aquellos de industria, ahora cada uno representando el 21.8% y 18.3% respectivamente. En 2010 estos dos juntos representaban el 27.5% del sector e incrementaron a representar el 32% del total de la zona. A los 12, 22 y 33 kilómetros de distancia, correspondiendo principalmente a las zonas de Guadalupe, San Nicolás de los Garza, Santa Catarina, Cumbres, Juárez y García, sucedió otro considerable incremento en empleos, particularmente en los ámbitos comerciales e industriales, con incrementos totales del 11.7%, 66% y 25.2% respectivamente.',
    '2015_2' : 'Esto marca una tendencia a la consolidación del centro, particularmente en los sectores terciarios, así como el continuo crecimiento de otros núcleos a mayor distancia. La productividad de estos nuevos centros de empleos dependerá de la accesibilidad a ellos por parte de la población y la facilidad de movilidad en la ciudad. Es posible que los viajes entre subnúcleos se vuelvan cada vez más relevantes, sin la necesidad de pasar por el núcleo previamente consolidado. El centro histórico sufrió incluso una pérdida de empleos del 10%.',
    '2019_1' : 'Al 2019 el centro consolidado entre los 3 y 7 kilómetros de distancia vio un fuerte desarrollo de empleos. Esta zona correspondiente principalmente a San Pedro Garza García y al Tecnológico de Monterrey vio un crecimiento del 11%, sin embargo, ha perdido relevancia en cuanto a concentración de empleos. En este año concentró el 31.8% de los empleos del área metropolitana, a comparación del 35% y 33% que concentraba en el año 2010 y 2015 respectivamente. Al año 2019 se mantienen las tendencias de crecimiento que se observaron en el 2015. Se nota una fuerte consolidación de empleos a 12 kilómetros, coincidiendo con las zonas de Cumbres, Santa Catarina, San Nicolás de los Garza y Guadalupe, con un aumento del 18.5%, correspondiente a más de 12,000 empleos. En el centro previamente consolidado a 6 kilómetros existe de igual forma un fuerte incremento en empleos de comercio y de oficina, habiendo aumentado por 16% y 28% respectivamente a comparación del 2015. La industria cobró mayor importancia entre los 19 y 22 kilómetros del centro, correspondiente a Santa Catarina, Mitras, Juárez, Escobedo y Apodaca. Se vio un incremento del 34% respecto a 2015 y representó el 47% de los empleos totales. La tendencia de empleos muestra un incremento en centros de empleabilidad a lo largo de la zona metropolitana y una disminución en la dependencia del centro histórico de la ciudad.',
    '2019_2' : 'En el aspecto global del área metropolitana, los empleos totales incrementaron por el 14%, siendo los empleos de oficina el sector con mayor crecimiento, del 20.7% respecto a 2015. La industria y el comercio tuvieron un crecimiento cercano, del 19.7% y 19.6% respectivamente. Sin embargo, el comercio sigue siendo la principal fuente de empleo del área metropolitana, representando el 36% de los empleos totales. La industria representó el 23% y los empleos de oficina y servicios representaron el 15% y 10% respectivamente.'
}



def get_denue(year='2019'):
    if year==None:
        year = '2019'
    
    fig_denue = go.Figure()
    for feature in available_denue:
        fig_denue.add_trace(go.Scatter(x=df_denue.query('anno=='+year)['dist_cbd'], y=df_denue.query('anno=='+year)[feature],
                    mode='lines',
                    name=feature))

    fig_denue.update_layout(
    xaxis_title="Distancia a centro de la ciudad",
    yaxis_title="Número de trabajos"
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
        yaxis_title="Número de personas"
    )

    return fig_censo

def get_mapa(row="dist_cbd"):
    if row==None:
        row = "dist_cbd"
    distance = px.choropleth_mapbox(df_concen, geojson = radio, color = row, locations = "dist_cbd", featureidkey= "properties.distance", center = {"lat": 25.668289, "lon": -100.310015}, mapbox_style='carto-positron', zoom=8.5)
    distance.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return distance


denue_options = dcc.Dropdown(
    options=[
        {'label': 'Actividades económicas 2010', 'value': '2010'},
        {'label': 'Actividades económicas 2015', 'value': '2015'},
        {'label': 'Actividades económicas 2019', 'value': '2019'},
    ],
    id = "denue-options",
    value='2019',
    clearable=False
)  

tab_denue = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4("Actividades Económicas", className = "card-title"),
            html.Hr(), 
            denue_options,
            dcc.Graph(
                id = "grafica_denue"
            ),
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
                figure = get_censo()
            )
        ],
        className = "mt-3"
    )   
)



tab_about = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4("Sobre la forma urbana", className = "card-title"),
            html.Hr(), 
            html.P("Phasellus id sem eu tortor mollis pharetra. Curabitur eleifend sapien sed fringilla auctor. Curabitur commodo vitae est non auctor. Quisque in iaculis dolor. Cras ut leo at ex fermentum facilisis id at quam. Nullam varius mi scelerisque, rhoncus lectus quis, efficitur dui. Duis vitae sapien sed leo euismod aliquam. Praesent luctus euismod odio, non convallis leo consequat ut. Praesent rhoncus lorem in felis luctus euismod. Donec eu mauris gravida, dignissim ante a, sollicitudin felis. Pellentesque interdum vitae nisi ac auctor. Mauris hendrerit viverra tempor. Etiam fringilla tincidunt aliquam. Proin sit amet odio quam. Morbi quis massa rutrum, pellentesque dui vitae, vulputate nunc. Proin facilisis nulla a pretium condimentum. ",className = "card-text"),
            html.P("In vel fringilla arcu. In imperdiet nisi rhoncus odio tincidunt, sit amet congue nisl bibendum. Mauris et justo ligula. Ut eget pretium augue. Curabitur porttitor orci in metus tincidunt cursus. Nam et massa volutpat, bibendum ipsum id, sodales diam. Integer faucibus quam et libero aliquam eleifend. Cras pulvinar fermentum semper. Fusce vitae efficitur leo, eget faucibus erat. Nullam tristique fermentum vehicula. Sed iaculis, felis dapibus tempor dapibus, eros nulla tincidunt elit, non egestas magna justo in ipsum. Aenean at sagittis nibh, sit amet iaculis lacus. Duis ut vestibulum elit, sed posuere erat. Etiam et vestibulum enim. Aenean consequat nisi id finibus lobortis. Praesent et nulla eu sem porttitor pulvinar.", className = "card-text"),
            html.P("Duis facilisis, lorem vitae mattis iaculis, purus purus scelerisque est, ac gravida orci nisl eget enim. Phasellus nulla arcu, mattis id tristique vel, fermentum non metus. Integer tristique tellus eget porta ultricies. Duis porta nisi eu eleifend accumsan. Nunc eget quam ut ipsum ultricies aliquam nec quis risus. Fusce egestas orci congue elit maximus bibendum. Nunc accumsan molestie mauris, eget suscipit dui tincidunt ac. Cras id ipsum ac metus lacinia euismod at a leo. Sed lacus erat, finibus aliquam enim sit amet, posuere faucibus orci. Vivamus pharetra finibus ligula, ac feugiat velit feugiat nec. Nullam enim justo, eleifend ac consectetur id, fermentum a ex. Aenean congue tempor odio, sit amet dictum purus congue ut.", className = "card-text"),
            html.P("Donec luctus id tellus nec feugiat. Morbi suscipit arcu a massa consequat sodales. Cras non sem ante. Praesent interdum lacus in metus condimentum, vitae pretium enim sagittis. Ut tellus enim, lobortis at justo tincidunt, posuere malesuada leo. Aenean quis tortor sed diam ultrices lobortis vel vitae erat. Nunc rhoncus molestie nulla ut cursus. Etiam vitae porttitor nulla. Etiam tempor cursus neque, sed rutrum enim tincidunt a. Vivamus felis enim, tristique eget eros eu, rhoncus mollis nibh. Aliquam non justo placerat tortor tempus dictum et nec urna.", className = "card-text")        
        ],
        className = "mt-3"
    )   
)

map_distancia = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4("Distancia al centro de la ciudad", className = "card-title"),
            dcc.Graph(
                figure = get_mapa('dist_cbd')
            )
        ],
    )   
)

map_empleo = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4("Diferencia de empleos 2010-2019", className = "card-title"),
            dcc.Graph(
                figure = get_mapa('Emp10_19')
            ),
        ],
    )   
)
map_poblacion = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4("Diferencia de población 2000-2016", className = "card-title"),
            dcc.Graph(
                figure = get_mapa('Pop0_16')
            )
        ]
    )   
)

map_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Distancia al centro", tab_id="maptab-1"),
                dbc.Tab(label="Diferencia empleo", tab_id="maptab-2"),
                dbc.Tab(label="Diferencia poblacion", tab_id="maptab-3")

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
                dbc.Tab(label="Población y vivienda", tab_id="tab-2"),
                dbc.Tab(label="Forma urbana", tab_id="tab-3")

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
                    md = 6,
                    children = [
                        tabs
                    ]
                ),
                dbc.Col(
                    md = 6,
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
    elif at == "tab-3":
        return tab_about
    return html.P("Error al cargar!...")

@app.callback(Output("mapcontent", "children"), [Input("maptabs", "active_tab")])
def switch_maptab(at):
    if at == "maptab-1":
        return map_distancia
    elif at == "maptab-2":
        return map_empleo
    elif at == "maptab-3":
        return map_poblacion
    return html.P("Error al cargar!...")

@app.callback([Output("grafica_denue", "figure"), Output("p_act1", "children"), Output("p_act2", "children")], [Input("denue-options", "value")])
def select_figure(selected_year):
    return get_denue(selected_year), empleos_content[selected_year+'_1'], empleos_content[selected_year+'_2']



if __name__ == '__main__':
    app.run_server(debug=True)

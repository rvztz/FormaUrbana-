import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input 
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Forma Urbana Zona Metropolitana Mty'
app.config.suppress_callback_exceptions = True

df_censo = pd.read_csv('~/Documents/Workspace/EUrb/CensoMTY2000_10_16CBD.csv')
df_concen = pd.read_csv("~/Documents/WorkSpace/EUrb/GradientesPop_Jobs.csv")
df_denue = pd.read_csv('~/Documents/WorkSpace/EUrb/DENUEMTYCBD_2010_15_19.csv')
available_denue = ['comercio','industria', 'oficina', 'servicios'] 
radio = json.load(open('/Users/RogerVazquezT/Documents/WorkSpace/EUrb/MapaGradientes.json'))


acerca_de = dbc.NavItem(dbc.NavItem(dbc.NavLink("Acerca de", href = "#")))

contactanos = dbc.NavItem(dbc.NavItem(dbc.NavLink("Equipo", href = "#")))


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
            html.P("Phasellus id sem eu tortor mollis pharetra. Curabitur eleifend sapien sed fringilla auctor. Curabitur commodo vitae est non auctor. Quisque in iaculis dolor. Cras ut leo at ex fermentum facilisis id at quam. Nullam varius mi scelerisque, rhoncus lectus quis, efficitur dui. Duis vitae sapien sed leo euismod aliquam. Praesent luctus euismod odio, non convallis leo consequat ut. Praesent rhoncus lorem in felis luctus euismod. Donec eu mauris gravida, dignissim ante a, sollicitudin felis. Pellentesque interdum vitae nisi ac auctor. Mauris hendrerit viverra tempor. Etiam fringilla tincidunt aliquam. Proin sit amet odio quam. Morbi quis massa rutrum, pellentesque dui vitae, vulputate nunc. Proin facilisis nulla a pretium condimentum. ",className = "card-text"),
            html.P("In vel fringilla arcu. In imperdiet nisi rhoncus odio tincidunt, sit amet congue nisl bibendum. Mauris et justo ligula. Ut eget pretium augue. Curabitur porttitor orci in metus tincidunt cursus. Nam et massa volutpat, bibendum ipsum id, sodales diam. Integer faucibus quam et libero aliquam eleifend. Cras pulvinar fermentum semper. Fusce vitae efficitur leo, eget faucibus erat. Nullam tristique fermentum vehicula. Sed iaculis, felis dapibus tempor dapibus, eros nulla tincidunt elit, non egestas magna justo in ipsum. Aenean at sagittis nibh, sit amet iaculis lacus. Duis ut vestibulum elit, sed posuere erat. Etiam et vestibulum enim. Aenean consequat nisi id finibus lobortis. Praesent et nulla eu sem porttitor pulvinar.", className = "card-text")

        ],
        className = "mt-3"
    )   
)

tab_censo = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4("Población y vivienda 2000/2016", className = "card-title"),
            html.Hr(),
            html.P("Phasellus id sem eu tortor mollis pharetra. Curabitur eleifend sapien sed fringilla auctor. Curabitur commodo vitae est non auctor. Quisque in iaculis dolor. Cras ut leo at ex fermentum facilisis id at quam. Nullam varius mi scelerisque, rhoncus lectus quis, efficitur dui. Duis vitae sapien sed leo euismod aliquam. Praesent luctus euismod odio, non convallis leo consequat ut. Praesent rhoncus lorem in felis luctus euismod. Donec eu mauris gravida, dignissim ante a, sollicitudin felis. Pellentesque interdum vitae nisi ac auctor. Mauris hendrerit viverra tempor. Etiam fringilla tincidunt aliquam. Proin sit amet odio quam. Morbi quis massa rutrum, pellentesque dui vitae, vulputate nunc. Proin facilisis nulla a pretium condimentum. ",className = "card-text"),
            html.P("In vel fringilla arcu. In imperdiet nisi rhoncus odio tincidunt, sit amet congue nisl bibendum. Mauris et justo ligula. Ut eget pretium augue. Curabitur porttitor orci in metus tincidunt cursus. Nam et massa volutpat, bibendum ipsum id, sodales diam. Integer faucibus quam et libero aliquam eleifend. Cras pulvinar fermentum semper. Fusce vitae efficitur leo, eget faucibus erat. Nullam tristique fermentum vehicula. Sed iaculis, felis dapibus tempor dapibus, eros nulla tincidunt elit, non egestas magna justo in ipsum. Aenean at sagittis nibh, sit amet iaculis lacus. Duis ut vestibulum elit, sed posuere erat. Etiam et vestibulum enim. Aenean consequat nisi id finibus lobortis. Praesent et nulla eu sem porttitor pulvinar.", className = "card-text"),
            html.P("Duis facilisis, lorem vitae mattis iaculis, purus purus scelerisque est, ac gravida orci nisl eget enim. Phasellus nulla arcu, mattis id tristique vel, fermentum non metus. Integer tristique tellus eget porta ultricies. Duis porta nisi eu eleifend accumsan. Nunc eget quam ut ipsum ultricies aliquam nec quis risus. Fusce egestas orci congue elit maximus bibendum. Nunc accumsan molestie mauris, eget suscipit dui tincidunt ac. Cras id ipsum ac metus lacinia euismod at a leo. Sed lacus erat, finibus aliquam enim sit amet, posuere faucibus orci. Vivamus pharetra finibus ligula, ac feugiat velit feugiat nec. Nullam enim justo, eleifend ac consectetur id, fermentum a ex. Aenean congue tempor odio, sit amet dictum purus congue ut.", className = "card-text"),
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
            html.P("Phasellus id sem eu tortor mollis pharetra. Curabitur eleifend sapien sed fringilla auctor. Curabitur commodo vitae est non auctor. Quisque in iaculis dolor. Cras ut leo at ex fermentum facilisis id at quam. Nullam varius mi scelerisque, rhoncus lectus quis, efficitur dui. Duis vitae sapien sed leo euismod aliquam. Praesent luctus euismod odio, non convallis leo consequat ut. Praesent rhoncus lorem in felis luctus euismod. Donec eu mauris gravida, dignissim ante a, sollicitudin felis. Pellentesque interdum vitae nisi ac auctor. Mauris hendrerit viverra tempor. Etiam fringilla tincidunt aliquam. Proin sit amet odio quam. Morbi quis massa rutrum, pellentesque dui vitae, vulputate nunc. Proin facilisis nulla a pretium condimentum. ",className = "card-text"),
            html.P("In vel fringilla arcu. In imperdiet nisi rhoncus odio tincidunt, sit amet congue nisl bibendum. Mauris et justo ligula. Ut eget pretium augue. Curabitur porttitor orci in metus tincidunt cursus. Nam et massa volutpat, bibendum ipsum id, sodales diam. Integer faucibus quam et libero aliquam eleifend. Cras pulvinar fermentum semper. Fusce vitae efficitur leo, eget faucibus erat. Nullam tristique fermentum vehicula. Sed iaculis, felis dapibus tempor dapibus, eros nulla tincidunt elit, non egestas magna justo in ipsum. Aenean at sagittis nibh, sit amet iaculis lacus. Duis ut vestibulum elit, sed posuere erat. Etiam et vestibulum enim. Aenean consequat nisi id finibus lobortis. Praesent et nulla eu sem porttitor pulvinar.", className = "card-text")
        ],
    )   
)
map_poblacion = dbc.Card(
    dbc.CardBody(
        children = [
            html.H4("Diferencia de población 2000-2016", className = "card-title"),
            dcc.Graph(
                figure = get_mapa('Pop0_16')
            ), 
            html.P("Phasellus id sem eu tortor mollis pharetra. Curabitur eleifend sapien sed fringilla auctor. Curabitur commodo vitae est non auctor. Quisque in iaculis dolor. Cras ut leo at ex fermentum facilisis id at quam. Nullam varius mi scelerisque, rhoncus lectus quis, efficitur dui. Duis vitae sapien sed leo euismod aliquam. Praesent luctus euismod odio, non convallis leo consequat ut. Praesent rhoncus lorem in felis luctus euismod. Donec eu mauris gravida, dignissim ante a, sollicitudin felis. Pellentesque interdum vitae nisi ac auctor. Mauris hendrerit viverra tempor. Etiam fringilla tincidunt aliquam. Proin sit amet odio quam. Morbi quis massa rutrum, pellentesque dui vitae, vulputate nunc. Proin facilisis nulla a pretium condimentum. ",className = "card-text"),
            html.P("In vel fringilla arcu. In imperdiet nisi rhoncus odio tincidunt, sit amet congue nisl bibendum. Mauris et justo ligula. Ut eget pretium augue. Curabitur porttitor orci in metus tincidunt cursus. Nam et massa volutpat, bibendum ipsum id, sodales diam. Integer faucibus quam et libero aliquam eleifend. Cras pulvinar fermentum semper. Fusce vitae efficitur leo, eget faucibus erat. Nullam tristique fermentum vehicula. Sed iaculis, felis dapibus tempor dapibus, eros nulla tincidunt elit, non egestas magna justo in ipsum. Aenean at sagittis nibh, sit amet iaculis lacus. Duis ut vestibulum elit, sed posuere erat. Etiam et vestibulum enim. Aenean consequat nisi id finibus lobortis. Praesent et nulla eu sem porttitor pulvinar.", className = "card-text")
        ],
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



data_menu = dbc.DropdownMenu(
    children = [
        dbc.DropdownMenuItem("Forma Urbana"),
        dbc.DropdownMenuItem("Atlas de calles"),
        dbc.DropdownMenuItem(divider = True),
        dbc.DropdownMenuItem("Descargas")
    ],
    nav = True,
    in_navbar = True, 
    label = "Investigación"
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand("Expansión urbana", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="#",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(dbc.Nav(
            [data_menu,acerca_de, contactanos], className = "ml-auto", navbar = True
        ),
         id="navbar-collapse", navbar=True),
    ],
    color = "dark",
    dark = True,

)


app.layout = html.Div(
    children = [
        navbar, 

    dbc.Container(
        fluid=True,
        children=[
        html.Div(
            className = "mt-3 mb-3",
            children =[
            html.H2(children ="Forma urbana de la Zona Metropolitana de Monterrey"),
            html.P(
                children="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consequat nunc et egestas condimentum. Donec pellentesque elit id suscipit ornare. Phasellus id sagittis erat. Pellentesque ullamcorper fermentum ipsum. Aenean massa."
            ),
            html.Hr()
            ]), 
    
  
    
        dbc.Row(
            align = "center",
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

@app.callback(Output("grafica_denue", "figure"), [Input("denue-options", "value")])
def select_figure(selected_year):
    return get_denue(selected_year)



if __name__ == '__main__':
    app.run_server(debug=True)

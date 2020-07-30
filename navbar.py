import dash_bootstrap_components as dbc
import dash_html_components as html


def Navbar():
    
    costos = dbc.NavItem(dbc.NavItem(dbc.NavLink("Costos", href = "https://expansionurbanamty.github.io/Website/index.html")))
    forma_urbana = dbc.NavItem(dbc.NavItem(dbc.NavLink("Forma urbana", href = "/apps/denue")))
    egresos = dbc.NavItem(dbc.NavItem(dbc.NavLink("Ingresos y egresos", href = "/apps/egresos")))
    atlas_calles = dbc.NavItem(dbc.NavItem(dbc.NavLink("Atlas de calles", href = "https://expansionurbanamty.github.io/Website/atlas.html")))
    equipo = dbc.NavItem(dbc.NavItem(dbc.NavLink("Equipo", href = "#")))
    metodologia = dbc.NavItem(dbc.NavItem(dbc.NavLink("Metodología", href = "#")))

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
                href="https://expansionurbanamty.github.io/Website/index.html",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(dbc.Nav(
                [costos,forma_urbana,egresos,atlas_calles,metodologia,equipo], className = "ml-auto", navbar = True
            ),
            id="navbar-collapse", navbar=True),
        ],
        color = "dark",
        dark = True,

    )

    return navbar


import dash
import dash_html_components as html
import dash_core_components as dcc

from .. import WebvizPluginABC

class MinimalPlugin(WebvizPluginABC):
    @property
    def layout(self):
        return html.Div([html.H1("This is a static title"),
                         "just some text"
                         ])
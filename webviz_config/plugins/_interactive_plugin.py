import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

"""
This application should simply display the text you enter
"""

from .. import WebvizPluginABC


class InteractivePlugin(WebvizPluginABC): # base class

    def __init__(self, app: Dash, title: str):
        super().__init__() #Calling the initializer of the baseclass WebcvizPluginABC
        self.title = title
        self.set_callbacks(app)

    @property # Function decorator that allows you to access layout method as an attribute
    def layout(self):
        return html.Div([dcc.Input(id='textfield', value='', type='text'), html.Div(id='my-div')])


    def set_callbacks(self, app: Dash):
        # Function decorator that
        @app.callback(
            Output(component_id='my-div', component_property='children'),
            [Input(component_id='textfield', component_property='value')]
        )
        def update_output(input_value):
            return f'You wrote: {input_value}'

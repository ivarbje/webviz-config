import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .. import WebvizPluginABC

"""
First step is to display a graph objed
"""

class TrajectoryGraph():
    
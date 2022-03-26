"""
This module takes care of starting the API Server, Adding the endpoints
"""
import os
import dash_bootstrap_components as dbc
from flask import Flask, jsonify, send_from_directory
from dash import Dash
from dash_app.layout import render_layout

ENV = os.getenv("FLASK_ENV")

external_stylesheets=[dbc.themes.BOOTSTRAP]

server = Flask(__name__)
app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    server=server,
)

# render dashboard
render_layout(app)

# this only runs if `$ python src/main.py` is executed
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3001))
    app.run(host="0.0.0.0", port=PORT, debug=True)

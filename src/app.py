import os
import dash_bootstrap_components as dbc
from dash import Dash
from flask import Flask
from layout import app_layout


external_stylesheets=[dbc.themes.BOOTSTRAP]
server = Flask(__name__)
app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    server=server,
)

# Start dashboard rendering
app_layout(app)
# End dashboard rendering
   
# this only runs if `$ python src/main.py` is executed
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3001))
    app.run(host="0.0.0.0", port=PORT, debug=True)

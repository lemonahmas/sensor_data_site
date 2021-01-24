from flask import Flask
import os

from flask.helpers import get_debug_flag

app = Flask("sensor_data")
app.debug = True
@app.route("/")
def main_page():
    app_name = app.import_name
    return f"Hello! This site is {app_name}."

if __name__ == "__main__":
    app.run()
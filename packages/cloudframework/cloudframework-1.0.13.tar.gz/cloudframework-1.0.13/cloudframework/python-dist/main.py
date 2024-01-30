# CLOUDFRAMEOWRK.io Python main.py
#
# This file will start you Python Server to create your company/project APIS.
# Also it will help you to interact with our CLOUD-PLAFORM


import os
from flask import Flask
from cloudframework import CoreFlask
#from tmp import _cloudframework
#from _cloudframework import CoreFlask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/', methods=["GET", "POST","PUT","DELETE","OPTIONS","DISPATCH"])
def main_root():
    # Catch every route
    # Create the object core
    core = CoreFlask(app,os.path.dirname(os.path.abspath(__file__)))
    return core.dispatch()

@app.route('/<path:path>', methods=["GET", "POST","PUT","DELETE","OPTIONS","DISPATCH"])
def main(path):
    # Catch every route
    # Create the object core

    core = CoreFlask(app,os.path.dirname(os.path.abspath(__file__)))
    return core.dispatch()

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.

    app.run(host='127.0.0.1', port=8080, debug=True)
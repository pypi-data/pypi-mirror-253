"""Flask API app creator module"""

from __future__ import absolute_import
import sys
import os
# +++++++++++++++++
BASE_PATH = os.path.abspath("./arya-helpers/Codes/src")
extendPaths = [p for p in (os.path.dirname(BASE_PATH), BASE_PATH) if p not in sys.path]
sys.path = extendPaths + sys.path
# +++++++++++++++++
from flask import Flask
from logmanager import configure_logging
from appconfig import CONFIG


def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False

    from . import aryaapis, explanationapi
    app.register_blueprint(aryaapis.bp)
    app.register_blueprint(explanationapi.bp)

    apps = [__name__, 'apiroutes', 'aryatestbed', 'joboperations']
    configure_logging(apps=apps, config=CONFIG['logging']['aryahelpers'])

    @app.route('/isalive')
    def isalive():
        return ('<b style="color:blue;">Alive</b> - Aryahelper APIs')
    return app

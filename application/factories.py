from flask import Flask
from application.views import api_views

def create_app(app_name, dotted_config_path=None):

    if dotted_config_path is None:
        dotted_config_path = 'application.config.base.Config'

    app = Flask(app_name)
    app.config.from_object(dotted_config_path)
    app.register_blueprint(api_views)
    return app

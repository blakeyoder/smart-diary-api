from flask import Blueprint, jsonify
from application.modules.api_views import INDEX_VIEW

api_views = Blueprint('api', __name__)

api_views.add_url_rule('/', view_func=INDEX_VIEW)

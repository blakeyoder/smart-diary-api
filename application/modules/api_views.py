from flask import jsonify
from flask.views import MethodView

class IndexView(MethodView):

    def get(self):
        return jsonify({'Hello': 'World!'})

INDEX_VIEW = IndexView.as_view('index')

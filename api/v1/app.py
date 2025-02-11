#!/usr/bin/python3
"""
    run flask
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
Cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """404 error handler"""
    msg = {"error": "Not found"}
    return jsonify(msg), 404


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", default="0.0.0.0")
    port = getenv("HBNB_API_PORT", default=5000)
    app.run(host=host, port=port, threaded=True)

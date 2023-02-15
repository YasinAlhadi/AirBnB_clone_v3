#!/usr/bin/python3
"""
    instance of Blueprint
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """returns a JSON status"""
    stat = {"status": "OK"}
    return jsonify(stat)


@app_views.route('/stats')
def stats():
    """retrieves the number of each objects by type"""
    classes = {"amenities": "Amenity", "cities": "City",
               "places": "Place", "reviews": "Review",
               "states": "State", "users": "User"}
    stats = {}
    for key, value in classes.items():
        stats[key] = storage.count(value)
    return jsonify(stats)

#!/usr/bin/python3
"""State module"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models import city
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_all():
    """Retrieves the list of all City objects of a State"""
    cities_list = []
    cities = storage.all('City')

    get_state = storage.get('State', state_id)
    if get_state is None:
        abort(404)

    for city in cities.values():
        if city.state_id == state_id:
            cities_list.append(city.to_dict())
    return jsonify(cities_list)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_method_city(city_id):
    """Retrieves a City object"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_method(city_id):
    """ delete city by id"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_obj():
    """create new instance"""
    js = request.get_json()
    if not js:
        abort(400, 'Not a JSON')
    if 'name' not in js:
        abort(400, 'Missing name')
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    new_city = City(**js)
    new_city.state_id = state_id
    storage.new(new_city)
    storage.save()
    storage.close()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def post_method(city_id):
    """post method"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    obj = storage.get('City', city_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict()), 200

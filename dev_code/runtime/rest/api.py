# -*- coding: utf-8 -*-
import json, yaml
from flask import Blueprint, session, request, make_response, \
    jsonify, url_for, abort

# Need to change the root PYTHONPATH during runtime
from dev_code.runtime.system.system_interface import *
# from runtime.system.system_interface import *

api = Blueprint('APIs', __name__)


@api.route("/", methods=['GET'])
def index(request):
    pass


@api.route("/create_lab", methods=['POST'])
def create_lab():
    if request.method == 'POST':
        data_json = json.dumps(request.get_json())
        data_dict = yaml.safe_load(data_json)
        lab_dict = {
            'id': data_dict['id'],
            'name': data_dict['name'],
            'overview': data_dict['overview'],
            'sections': data_dict['sections']
        }


@api.route("/create_experiment", methods=['POST'])
def create_experiment():
    if request.method == 'POST':
        data_json = json.dumps(request.get_json())
        data_dict = yaml.safe_load(data_json)
        experiment_dict = {
            'id': data_dict['id'],
            'name': data_dict['name'],
            'overview': data_dict['overview'],
            'sections': data_dict['sections']
        }
        try:
            SystemInterface.create_experiment(experiment_dict)
            return make_response("OK", 200)
        except:
            return make_response("NOT OK")

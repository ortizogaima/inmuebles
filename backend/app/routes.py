from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"mensaje": "Hola desde Flask!"})

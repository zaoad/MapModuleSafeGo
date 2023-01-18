from flask import Flask, request, Response, jsonify, render_template
from map_operations import *

app = Flask(__name__)


@app.route('/find_path/<source>/<destination>', methods=['GET'])
def find_path(source, destination):
    source, destination = list(map(float, source.split(','))), list(map(float, destination.split(',')))
    path_series = get_shortest_road_path(source, destination)
    resp = jsonify({'msg': 'Success', 'path': path_series.values.tolist()})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# @app.route('/',methods=["GET"])
@app.route('/<source>/<destination>', methods=["GET"])
def map_app(source, destination):
    return render_template('map.html', source=source, destination=destination)


@app.route('/', methods=["GET"])
def home():
    return '<h1>Safe go map</h1>'

if __name__ == '__main__':
    app.run(host="0.0.0.0")

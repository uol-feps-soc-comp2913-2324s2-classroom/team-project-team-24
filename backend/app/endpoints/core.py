from flask import Blueprint
from app.gpx import GPX
from flask import Response

bp = Blueprint('core', __name__, url_prefix='/core')

@bp.route('/map', methods=['GET'])
def serve_map():
    gpx_instance = GPX('track1.gpx')  # Replace with your GPX file
    map_html = gpx_instance.display()
    return Response(map_html, mimetype='text/html')
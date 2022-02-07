from flask import jsonify,Blueprint
from datetime import datetime
import logging

apiview = Blueprint('apiview', __name__)


@apiview.route('/api/apitest')
def apitest():
    return jsonify({'datetime': datetime.now(),'from':'api'})
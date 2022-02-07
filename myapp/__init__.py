

from flask import Flask
from logging import Logger
import logging
from myapp.views.views import view
from myapp.views.api import apiview
import os



app = Flask(__name__)
app.config.from_object('config')
app.config['APPDIR'] = os.getcwd()


if app.config['PROD']:
    logging.basicConfig(level=app.config['LOGLEVEL'],
                        format='%(levelname)s:%(asctime)s-%(filename)s-%(module)s-%(lineno)d:%(message)s',
                        filename=os.path.join(app.config['APPDIR'],'myapp','logs','app.log'))
else:
    logging.basicConfig(level=app.config['LOGLEVEL'],
                        format='%(levelname)s:%(asctime)s-%(filename)s-%(module)s-%(lineno)d:%(message)s'
                        )

app.register_blueprint(view)
app.register_blueprint(apiview)


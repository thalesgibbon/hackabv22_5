from flask import Flask, request, Response
from random import randrange
import os


app = Flask(__name__)


@app.route("/")
def index():
    driver_id = request.args.get('driver_id')
    if not driver_id:
        return {'driver_id': driver_id, 'score_good_driver': None, 'msg': 'driver_id obrigatorio'}, 400
    elif driver_id in os.listdir('exports'):
        score_good_driver = randrange(100)
        result = {'driver_id': driver_id, 'score_good_driver': score_good_driver, 'msg': 'ok'}
        return result, 200
    else:
        result = {'driver_id': driver_id, 'score_good_driver': None, 'msg': 'id nao encontrado'}
        return result, 406


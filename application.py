import json
from flask import Flask, request
from youtube_model import ym


application = Flask(__name__)
application.debug=True


@application.route('/', methods=['GET'])
def run():
    return " "


@application.route('/', methods=['POST'])
def hook():
    data = request.get_json()
    preds = ym.predict(data)
    preds = json.dumps({'preds': preds.tolist()})
    return preds


if __name__ == '__main__':
    application.run(host='0.0.0.0')

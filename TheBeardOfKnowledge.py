from flask import Flask
from flask import request, jsonify
import json
from Controller.Twitter import get_all_tweets_from_user_timeline
from Controller.Propublica import get_specific_member

app = Flask(__name__)


@app.route('/twitter')
def twitter():
    timeline = get_all_tweets_from_user_timeline("lutherstrange")
    return jsonify(timeline)


@app.route('/legislator')
def legislator():
    leg_id = "S001202"
    a = get_specific_member(leg_id)
    print(a)
    return jsonify(a)


if __name__ == '__main__':
    app.run()

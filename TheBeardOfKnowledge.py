from flask import Flask
from flask import request, jsonify
import json
from Controller.Twitter import get_all_tweets_from_user_timeline
from Controller.Propublica import get_specific_member

app = Flask(__name__)


@app.route('/twitter/timeline/<senator_twitter_name>')
def twitter(senator_twitter_name):
    name = "lutherstrange"
    timeline = get_all_tweets_from_user_timeline(senator_twitter_name)
    return jsonify(timeline)


@app.route('/legislator/<legislator_id>')
def legislator(legislator_id):
    leg_id = "S001202"
    legislator_data = get_specific_member(legislator_id)
    return jsonify(legislator_data)


if __name__ == '__main__':
    app.run()

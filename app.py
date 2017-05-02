import os

import requests
import requests_cache

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

requests_cache.install_cache('github_cache', backend='sqlite', expire_after=60*60*24)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    url = "https://api.github.com/{0}".format(path)
    response_dict = requests.get(url).json()
    return jsonify(response_dict)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
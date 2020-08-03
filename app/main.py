from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/")
def hello():
    return "It's ALIVE!!!"

# Testing slack integration
@app.route("/slack-app", methods=['POST'])
def slack_app():
    data = request.json.get('challenge')
    return data


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8000)

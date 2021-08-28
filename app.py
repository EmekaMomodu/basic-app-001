from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def doHealthCheck():
    response = {'result': 'OK - healthy'}
    return response, 200


@app.route("/metrics")
def getMetrics():
    response = {'UserCount': 140, 'UserCountActive': 23}
    return response, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
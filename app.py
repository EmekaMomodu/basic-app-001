from flask import Flask
import logging

app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info('Main request successful')
    return "Hello World!"


@app.route("/status")
def doHealthCheck():
    response = {'result': 'OK - healthy'}
    app.logger.info('Status request successful')
    return response, 200


@app.route("/metrics")
def getMetrics():
    response = {'UserCount': 140, 'UserCountActive': 23}
    app.logger.info('Metrics request successful')
    return response, 200


if __name__ == "__main__":
    # stream logs to app.log file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(host='0.0.0.0')

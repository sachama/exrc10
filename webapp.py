
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
counter = 0

metrics = PrometheusMetrics(app)
metrics.start_http_server(5000)

@app.route("/app")
def test():
    global counter
    counter += 1
    return (f"You visit this page {counter}-times - sacha")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=6000)
"""
from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

app = Flask(__name__)
counter = 0

@app.route("/app")
def index():
    global counter
    counter += 1
    return (f"You visit this page {counter}-times - sacha")

# provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.1.2", app_config="staging")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

run_simple(hostname="0.0.0.0", port=5000, application=dispatcher)
"""
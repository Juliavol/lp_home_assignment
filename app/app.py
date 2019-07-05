import random

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter
from prometheus_client import Gauge

app = Flask(__name__)
PrometheusMetrics(app)


ic = Counter('int_counter', 'Description of counter')
fc = Counter('float_counter', 'Description of counter')
ig = Gauge('int_guage', 'Description of gauge')
fg = Gauge('float_guage', 'Description of gauge')

@app.route('/randomFloat')
def floatIndex():
    rand_float = random.uniform (0, 10)
    fc.inc(rand_float)
    fg.set(rand_float)

    return "ok float"

@app.route('/randomInt')
def intIndex():
    rand_int = random.randint(0, 1000)
    ic.inc(rand_int)
    ig.set(rand_int)
    return "ok int"


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)




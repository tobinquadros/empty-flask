# stdlib
import time
import random

# non-stdlib
from flask import Flask
from prometheus_client import start_http_server, Histogram, Gauge, Counter, Summary

app = Flask(__name__)
start_http_server(8000)

HISTOGRAM_BUCKETS = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

REQUEST_COUNT = Counter(
        'request_count',
        'Count of HTTP requests.',
        ['method', 'endpoint'],
        )
REQUEST_IN_PROGRESS = Gauge(
        'request_in_progress',
        'Number of requests in progress.',
        )
REQUEST_PROCESSING_SECONDS = Histogram(
        'request_processing_seconds',
        "Time spent processing the request.",
        ['method', 'endpoint'],
        buckets=HISTOGRAM_BUCKETS
        )
REQUEST_SUMMARY = Summary(
        'request_summary',
        'Summary of request'
        )

@app.route('/')
def index():
    with REQUEST_PROCESSING_SECONDS.labels(method='GET', endpoint='/').time():
        lag = random.normalvariate(2, 0.5)
        time.sleep(lag)
    return 'Flask was finished in {:0.2f} seconds.\n'.format(lag)

@app.route('/count')
def count():
    REQUEST_SUMMARY.observe(1)
    REQUEST_COUNT.labels(method='GET', endpoint='/count').inc()
    return 'counted'


if __name__ == '__main__':
    app.run()

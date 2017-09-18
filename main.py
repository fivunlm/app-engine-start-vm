import json
import httplib2
import logging
from apiclient import discovery
from google.appengine.api import memcache
from oauth2client.contrib.appengine import AppAssertionCredentials

from flask import Flask

app = Flask(__name__)

INSTANCE_NAME = 'vm-instance'
INSTANCE_ZONE = 'us-central1-c'
PROJECT = 'positive-shell-160220'

def get_http():
    credentials = AppAssertionCredentials(scope='https://www.googleapis.com/auth/compute')
    http = credentials.authorize(httplib2.Http(memcache))
    return http


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/vm/get')
def get_vm():
    http = get_http()
    uri = 'https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instances/{instance}'
    uri = uri.format(project=PROJECT, zone=INSTANCE_ZONE, instance=INSTANCE_NAME)
    resp, result = http.request(
        uri=uri,
        method='GET'
        )
    logging.debug(resp)
    logging.debug(result)
    return result, 200, {'Content-Type': 'application/json'}


@app.route('/vm/start')
def start_vm():
    http = get_http()
    uri = 'https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instances/{instance}/start'
    uri = uri.format(project=PROJECT, zone=INSTANCE_ZONE, instance=INSTANCE_NAME)
    resp, result = http.request(
        uri=uri,
        method='POST'
        )
    logging.debug(resp)
    logging.debug(result)
    return result, 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run()

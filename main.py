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


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/vm/start')
def start_vm():
    credentials = AppAssertionCredentials(scope='https://www.googleapis.com/auth/compute')
    http = credentials.authorize(httplib2.Http(memcache))
    compute = discovery.build('compute', 'v1', http=http)
    result = compute.instances().start(instance=INSTANCE_NAME, zone=INSTANCE_ZONE, project=PROJECT).execute()
    logging.debug(result)
    return json.dumps(result, indent=4)


if __name__ == '__main__':
    app.run()

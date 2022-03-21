#!/usr/bin/env python3
import os
import connexion
from werkzeug.routing import Rule
from openapi_server import encoder


app = connexion.App(__name__, specification_dir='../openapi_server/openapi')

APP_ROOT = os.getenv("APP_ROOT")
if APP_ROOT is not None:
    class CustomRule(Rule):
        def __init__(self, string, *args, **kwargs):
            if APP_ROOT.endswith('/'):
                prefix_without_end_slash = APP_ROOT.rstrip('/')
            else:
                prefix_without_end_slash = APP_ROOT
            if APP_ROOT.startswith('/'):
                prefix = prefix_without_end_slash
            else:
                prefix = '/' + prefix_without_end_slash
            super(CustomRule, self).__init__(prefix + string, *args, **kwargs)

    app.app.url_rule_class = CustomRule

app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Swagger Petstore'},
            pythonic_params=True)

if __name__ == '__main__':
    app.run()

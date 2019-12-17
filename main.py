from flask import Flask, request
import logging

app = Flask(__name__)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

@app.route('/', methods=HTTP_METHODS)
@app.route('/<path:path>', methods=HTTP_METHODS)
def hello_world(path=''):
    print(request.method, f'/{path}', request.headers, request.data)
    return 'ok'

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("port", default=8888, help="port")
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port)

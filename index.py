import os

from flask import Flask, jsonify, url_for, render_template, request, send_from_directory
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy
from helpers import get_env


app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = get_env('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = get_env('BASIC_AUTH_PASSWORD')
app.config['DEBUG'] = True

basic_auth = BasicAuth(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bmo/')
def bmo():
    secret = request.args.get('secret')
    
    return render_template('bmo.html', secret=secret)


@app.route('/argst/')
def argst():
    args = request.args
    stype = type(args)
    return render_template('args.html', args=args, stype=stype)



@app.route('/logs/')
@basic_auth.required
def logs():
    resp = { 'status': 123 }
    return jsonify(resp)



#@app.route('/test/')
#def test():
#    url = get_env('POSTGRES_URL')
#    return render_template('test.html', url=url)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

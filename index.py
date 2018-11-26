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



@app.route('/test/')
def test():
    item1 = {
        "title": "about our guild",
        "content": "This is all About our guild. We are wow guild and stuff. \
                    we like turtles, but respect the life cycle" }
    item2 = {
        "title": "Guild Activities",
        "content": "Sometimes we do mythic uldir, sometimes we kill heroic ghuun, some times we mythic+. once \
                    we did world pvp, dressing up like pilgrims and raiding SW. we did this on thanksgiving \
                    weekend so it was contextually sane. Also we killed many, MANY lowbies. I mean if they \
                    didnt want to get ganked in their capital city, they wouldnt have warmode on, right? RIGHT?!" }

    item3 = {
        "title": "Accomplishments",
        "content": "we hit AOTC on ANT and Uldir, we are try-hards sometimes but only made it 2/8 mythic uldir. \
                    people got totally burnt out and couldnt comprehend the mechanics for zek'voz. well, be \
                    pushing mythic next patch though, probably." }

    items = [item1, item2, item3]

    return render_template('three_cols.html', items=items)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

from flask import Flask, url_for, render_template, request, send_from_directory
from flask_basicauth import BasicAuth


app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'wtpa'
app.config['BASIC_AUTH_PASSWORD'] = 'l0g5'

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
    import os
    oot_dir = os.path.dirname(os.getcwd())

    return send_from_directory(os.path.join(root_dir, 'static', 'irc_logs'), '2018-06-27.txt')









if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

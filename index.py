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



@app.route('/about/')
def about():
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


@app.route('/roster/')
def roster():
    officers = {
        "title": "officers",
        "content": [
            "GM Blaineschar-Crushridge  Blaine",
            "Raid Leader Nemesis-Crushridge / Dahliadied-Crushridge  Hodgy",
            "Raid Leader Arinora-Anub'arak / Nexia-Anub'arak Zel",
            "Raid Leader Bano-Smolderthorn   Bano"]}
    raiders = {
        "title": "raiders",
        "content": [
            "Myroslav-???????",
            "Blaineschar-Crushridge",
            "Nemesis-Crushridge",
            "Arinora-Anub'arak",
            "Nexia-Anub'arak Zel",
            "Bano-Smolderthorn"]}

    m_plus = {
        "title": "M+ Teams",
        "content": "More to be announced" }

    items = [officers, raiders, m_plus]

    return render_template('three_cols.html', items=items)


@app.route('/events/')
def events():
    news = [
        { "title": "mythic progression",
          "content": "Mythic progression is on hold at Taloc and Mother until further notice or \
                      we get the numbers we need consistently to proceed. Plan on diving into Heroic for \
                      8.1.0 with Mythic starting a week or two after. Lets get this shit on farm!",
          "createdAt": "11.28.2018" },

        { "title": "new site",
          "content": "This is hte beginning of our new site. \
                      Special thanks to Myroslav for the layout and amazing voices.",
          "createdAt": "11.28.2018" }]
    events = [
        { "title": "Mythic Uldir",
          "description": "Taloc and Mother (for now)",
          "timeStart": "Tuesday 7pm CST (server)",
          "timeEnd": "Tuesday 10pm CST (server)" },
        { "title": "Heroic Uldir",
          "description": "Full Clear Heroic Uldir",
          "timeStart": "Thursday 7pm CST (server)",
          "timeEnd": "Thursday 10pm CST (server)" },
        { "title": "Mythic+ Day",
          "description": "A dedicated day for mythic+ runs for guildies.",
          "timeStart": "Friday 7pm CST (server)",
          "timeEnd": "Friday 10pm CST (server)" },
        { "title": "Whatevers Left",
          "description": "A flex day to finish whatever content we missed for the week.",
          "timeStart": "Sunday 7pm CST (server)",
          "timeEnd": "Sunday 10pm CST (server)" }]


    return render_template('two_rows_two_cols.html',
                           news=news,
                           events=events)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

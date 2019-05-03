from flask import Flask, render_template, request, g
import logging
import rdb
import os
from werkzeug.utils import redirect
from .views.topic import topic

app = Flask(__name__)
app.register_blueprint(topic, url_prefix='/topics')

@app.route('/')
def top():
    return render_template('top.html')

@app.teardown_request
def teardown_db(exception):
    print('start teardown_db')
    db = getattr(g, 'db', None)
    if db is not None:
        print('has db')
        db.close()
    else:
        print('has no db')

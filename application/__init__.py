from flask import Flask, render_template, request
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

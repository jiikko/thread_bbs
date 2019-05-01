from flask import Flask, render_template, request
import logging
import rdb
import os

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/')
def top():
    return render_template('top.html')

@app.route('/topics/new')
def topics_new():
    return render_template('topics/new.html')

@app.route('/topics', methods=['POST'])
def topics_create():
    logging.info('posted topics')
    rdb.insert_topics(title='title desu', body='body desu')

    return render_template('topics/new.html')

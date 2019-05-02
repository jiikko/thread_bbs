from flask import Flask, render_template, request
import logging
import rdb
import os
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/')
def top():
    return render_template('top.html')

@app.route('/topics/new', methods=['POST', 'GET'])
def topics_new():
    if request.method == 'POST':
        rdb.insert_topics(title=request.form['title'], body=request.form['body'])
        return redirect("/topics")
    else:
        return render_template('topics/new.html')

@app.route('/topics')
def topics_index():
    topics = rdb.fetch_all_topics()
    return render_template('topics/index.html', topics=topics)

@app.route('/topics/<id>')
def topics_show(id):
    topic = rdb.find_topic(id)
    return render_template('topics/show.html', topic=topic)

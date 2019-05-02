from flask import Blueprint, render_template, request
from werkzeug.utils import redirect
from application import rdb
import logging

topic = Blueprint('topic', __name__)

@topic.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        rdb.insert_topics(title=request.form['title'], body=request.form['body'])
        return redirect("/topics/")
    else:
        return render_template('topics/new.html')

@topic.route('/<id>/edit', methods=['POST', 'GET'])
def edit(id):
    logging.info(request.form)
    if request.method == 'POST':
        rdb.update_topic(id, title=request.form['title'], body=request.form['body'])
        return redirect("/topics/%s" % id)
    else:
        topic = rdb.find_topic(id)
        return render_template('topics/edit.html', topic=topic)

@topic.route('/')
def index():
    topics = rdb.fetch_all_topics()
    return render_template('topics/index.html', topics=topics)

@topic.route('/<id>')
def show(id):
    topic = rdb.find_topic(id)
    return render_template('topics/show.html', topic=topic)

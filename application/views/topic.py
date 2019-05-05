from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from application import rdb
import logging
from application.models.topic import Topic

topic = Blueprint('topic', __name__)

@topic.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        Topic({ 'title': request.form['title'], 'body': request.form['body'] }).save()
        return redirect("/topics/")
    else:
        return render_template('topics/new.html')

@topic.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    logging.info(request.form)
    if request.method == 'POST':
        rdb.update_topic(id, title=request.form['title'], body=request.form['body'])
        return redirect("/topics/%s" % id)
    else:
        topic = Topic.find(id)
        return render_template('topics/edit.html', topic=topic)

@topic.route('/')
def index():
    topics = rdb.fetch_all_topics()
    return render_template('topics/index.html', topics=topics)

@topic.route('/<int:id>')
def show(id):
    topic = Topic.find(id)
    return render_template('topics/show.html', topic=topic)

@topic.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    rdb.destroy_topic(id)
    return redirect('/topics/')

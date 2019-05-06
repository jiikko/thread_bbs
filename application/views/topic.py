from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
import logging
from application.models.topic import Topic
from application.models.comment import Comment

topic = Blueprint('topic', __name__)

@topic.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        Topic.create({ 'title': request.form['title'], 'body': request.form['body'] })
        return redirect(url_for('topic.index'))
    else:
        return render_template('topics/new.html')

@topic.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    topic = Topic.find(id)
    if request.method == 'POST':
        topic.update({ 'title': request.form['title'], 'body': request.form['body'] })
        return redirect(url_for('topic.show', id=id))
    else:
        topic = Topic.find(id)
        return render_template('topics/edit.html', topic=topic)

@topic.route('/')
def index():
    topics = Topic.all()
    return render_template('topics/index.html', topics=topics)

@topic.route('/<int:id>')
def show(id):
    topic = Topic.find(id)
    comments = topic.comments()
    return render_template('topics/show.html', topic=topic, comments=comments)

@topic.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    topic = Topic.find(id)
    topic.destroy()
    return redirect(url_for('topic.index'))

@topic.route('/<int:id>/comments/new', methods=['POST', 'GET'])
def new_comment(id):
    topic = Topic.find(id)
    if request.method == 'POST':
        Comment.create({ 'topic_id': topic.id(), 'body': request.form['comment_body'] })
        return redirect(url_for('topic.show', id=id))
    else:
        return render_template('comments/new.html', topic=topic)

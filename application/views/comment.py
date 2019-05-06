from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
import logging
from application.models.topic import Topic

topic_thead = Blueprint('commnt', __name__)
@topic.route('/show')

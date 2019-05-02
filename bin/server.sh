#!/bin/sh

yes | dev_appserver.py --watcher_ignore_re='(.*mysql|^/app/bin/.*|.*/tests/.*)' --env_var MYSQL_HOST=$MYSQL_HOST --host=0.0.0.0 .

import os
from base import EnvironmentBase

class EnvironmentDevelopment(EnvironmentBase):
    MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWD = ''
    MYSQL_DB = 'thread_bbs_development'
    MYSQL_CHARSET = 'utf8mb4'

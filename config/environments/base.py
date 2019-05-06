class EnvironmentBase(object):
    @classmethod
    def to_mysql_config(cls):
        MYSQL_CONFIG = {
            'host': cls.MYSQL_HOST,
            'user': cls.MYSQL_USER,
            'passwd':  cls.MYSQL_PASSWD,
            'db': cls.MYSQL_DB,
            'charset': cls.MYSQL_CHARSET,
        }
        return MYSQL_CONFIG

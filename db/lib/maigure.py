import MySQLdb

def create(mysql_config):
    db = mysql_config['db']
    del(mysql_config['db'])
    conn = MySQLdb.connect(**mysql_config)

    cursor = conn.cursor()
    cursor.execute('create database %s' % db)
    conn.select_db(db)
    print 'created %s' % db

    cursor.execute(create_meta_table_sql())
    print 'created meta table'

    cursor.close()
    conn.close()

def create_meta_table_sql():
    s = '''
CREATE TABLE `schema_versions` (
  `version` varchar(191) NOT NULL,
  PRIMARY KEY (`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
;
    '''
    return s

def migrate(mysql_config):
    import os
    import re

    conn = MySQLdb.connect(**mysql_config)
    cursor = conn.cursor()
    migration_path = 'db/migrations/'
    for path in os.listdir(migration_path):
        migration_version = re.match('^([\d]+)', path).group(0)
        cursor.execute('select 1 from schema_versions where version = "%s"' % migration_version)
        row = cursor.fetchone()
        if row == None:
            conn.begin()
            sql = open(migration_path + path).read()
            cursor.execute(sql)
            cursor.execute('insert into schema_versions (version) values ("%s")' % migration_version)
            conn.commit()
            print('done db migrate %s version' % migration_version)
        else:
            continue
    cursor.close()
    conn.close()

def drop(mysql_config):
    conn = MySQLdb.connect(**mysql_config)
    cursor = conn.cursor()
    cursor.execute('drop database %s' % mysql_config['db'])
    cursor.close()
    conn.close()
    print 'done drop "%s" databse' % mysql_config['db']

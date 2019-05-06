from db.lib import maigure
import config

maigure.create(config.env.to_mysql_config())

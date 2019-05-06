from db.lib import maigure
import config

maigure.drop(config.env.to_mysql_config())

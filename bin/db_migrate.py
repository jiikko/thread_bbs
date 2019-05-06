from db.lib import maigure
import config

maigure.migrate(config.env.to_mysql_config())

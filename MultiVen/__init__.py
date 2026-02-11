import pymysql

pymysql.version_info = (2, 2, 4, "final", 0) # Fake the version for Django
pymysql.install_as_MySQLdb()
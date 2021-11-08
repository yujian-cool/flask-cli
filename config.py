# 数据库配置
HOST = 'localhost'
PORT = '3306'
DATABASE = 'flask'
USERNAME = 'root'
PASSWORD = '123456'

# 本地数据库
# DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

# 服务编排
DB_URI = "mysql+pymysql://{username}:{password}@mysql/{db}?charset=utf8".format(username=USERNAME, password=PASSWORD,
                                                                                db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

# redis配置
REDIS_HOST = 'redis'
REDIS_PORT = '6379'
REDIS_PASSWORD = ''
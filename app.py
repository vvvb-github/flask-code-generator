from datetime import timedelta
from flask import Flask
from flask_cors import *
from config import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 解决跨域问题
CORS(app, supports_credentials=True)

# 缓存1秒，用来解决静态文件不刷新
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

# 设置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://' + mysql_user + ':' + mysql_pass + '@' + mysql_host + ':' + str(
        mysql_port) + '/' + mysql_name + '?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 创建数据库对象
db = SQLAlchemy(app=app)
db.create_all()

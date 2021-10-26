from flask import Flask
from flask_migrate import Migrate

from database.database import db

import config

app = Flask(__name__)

app.config.from_object(config)

migrate = Migrate(app, db)

# 按需引入
from model.model import User

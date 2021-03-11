import os
import sys

from flask import Flask
from flask_login import LoginManager

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # приложение

app.config['SECRET_KEY'] = 'our_project_secret_key'  # секретный ключ для csrf токена
app.config['UPLOAD_FOLDER'] = 'static\img\\'  # папка куда будут загружаться картинки пользователей
app.config['SECRET_KEY'] = 'our_project_secret_key'  # секретный ключ для csrf токена
app.config['UPLOAD_FOLDER'] = 'static/img/'  # папка куда будут загружаться картинки пользователей
app.config.from_object(Config)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
print(app.config.items())

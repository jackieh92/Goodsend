from flask import Flask
from config import Config


#Import for flask login
from flask_login import LoginManager
app = Flask(__name__)
app.config.from_object(Config)


login = LoginManager(app)
login.login_view = 'login' # Specify what page to load for NON-authenticated Users


from goodsend import routes,models

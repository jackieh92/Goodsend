from goodsend import app, login
from firebase_admin import credentials, firestore, initialize_app

#Import for Werkzeug Security
from werkzeug.security import generate_password_hash, check_password_hash

# Import for Date Time Module
from datetime import datetime

from flask_login import UserMixin
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin):

    cred = credentials.Certificate('./goodsend/key.json')
    default_app = initialize_app(cred)
    db = firestore.client()

    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.set_password(password)




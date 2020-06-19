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
    # Initialize Firestore DB
    cred = credentials.Certificate('./goodsend/key.json')
    default_app = initialize_app(cred)
    db = firestore.client()
    # ben_ref = db.collection('beneficiary')

    # id = db.Column(db.Integer, primary_key = True)
    # first_name = db.Column(db.String(150), nullable = False, unique = True)
    # last_name = db.Column(db.String(150), nullable = False, unique = True)
    # email = db.Column(db.String(150), nullable = False, unique = True)
    # password = db.Column(db.String(256),nullable = False)

    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    # def __repr__(self):
    #     return f'{self.first_name} has been created with {self.email}'

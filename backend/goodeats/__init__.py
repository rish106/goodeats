from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from goodeats.database import db
from goodeats.models import User 

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/recipedatabase'
app.config['SERVER_NAME'] = '127.0.0.1:5000'
app.config['WTF_CSRF_ENABLED'] = False
bcrypt = Bcrypt(app)
db.init_app(app)

from goodeats import routes

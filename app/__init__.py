from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


from app.routes.login_bp import login_bp
from app.routes.logout_bp import logout_bp
from app.routes.profile_bp import profile_bp
from app.routes.register_bp import register_bp
from app import models, topRoutes

app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(logout_bp, url_prefix="/logout")
app.register_blueprint(profile_bp, url_prefix="/profile")
app.register_blueprint(register_bp, url_prefix="/register")
db.create_all()


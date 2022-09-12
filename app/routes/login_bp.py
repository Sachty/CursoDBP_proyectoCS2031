from flask import Blueprint
from app.controllers.LoginController import login

login_bp = Blueprint('login_bp', __name__)

login_bp.route('/', methods=["GET", "POST"]) (login)
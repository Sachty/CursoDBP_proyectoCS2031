from flask import Blueprint
from app.controllers.RegisterController import register

register_bp = Blueprint('register_bp', __name__)

register_bp.route('/', methods=["GET", "POST"]) (register)
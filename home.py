from flask import Blueprint, send_file
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return send_file("./templates/index.html")
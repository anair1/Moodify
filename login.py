from flask import Blueprint
login_bp = Blueprint('login', __name__)

@login_bp.route("/")
def login():
    return "Need to integrate Spotify login", 404
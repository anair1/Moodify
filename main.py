from flask import Flask

from home import home_bp
from login import login_bp
from getrecs import getrecs_bp

app = Flask(__name__, static_folder="./assets")

app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(getrecs_bp, url_prefix='/recs')

app.run(debug=True)
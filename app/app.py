"""
flask app
"""
import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from routes.images import image_bp

load_dotenv()

app = Flask(__name__)
app.config.update(dict(SECRET_KEY=os.getenv(
    "SECRET_KEY"), DEBUG=os.getenv("DEBUG")))
CORS(app)

app.register_blueprint(image_bp, url_prefix="/images")

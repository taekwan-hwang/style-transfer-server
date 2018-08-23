"""run flask app"""
import os

from dotenv import load_dotenv
from app import app
load_dotenv()

app.run(host='0.0.0.0', port=os.getenv("PORT"))

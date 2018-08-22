"""run flask app"""
import os

from dotenv import load_dotenv
from app import app
load_dotenv()

app.run(port=os.getenv("PORT"))

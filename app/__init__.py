from flask import Flask
# Initialising application
app = Flask (__name__)

# Setting up configuration
app.config.from_object(DevConfig)

from app import views

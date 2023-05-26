from flask import abort, jsonify, redirect, render_template, request, url_for
from flask_migrate import Migrate
import sys

from init import create_app
from models import db

app = create_app()
# bootstrap database migrate commands
db.init_app(app)
migrate = Migrate(app, db)



if __name__ == "__main__":
    app.run(host="0.0.0.0")
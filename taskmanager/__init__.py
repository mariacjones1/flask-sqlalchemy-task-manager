import os
from flask import Flask  # noqa
from flask_sqlalchemy import SQLAlchemy  # noqa
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URL"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes  # noqa

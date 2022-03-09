import os
import sys

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL is None:
    print(
        "To run this module,"
        " you must set a `DATABASE_URL` environment variable - aborting ..."
    )
    sys.exit(1)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)

    issues = db.relationship(
        "Issue",
        backref="parent_project",
        cascade="all, delete, delete-orphan",
    )

    def __repr__(self):
        return f"<Project (id={self.id}, name={self.name})>"


class Issue(db.Model):
    __tablename__ = "issues"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)

    project_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "projects.id",
            ondelete="cascade",
        ),
        nullable=False,
    )

    def __repr__(self):
        return f"<Issue (id={self.id})>"


@app.route("/")
def home():
    r = jsonify({"message": "Hello World!"})
    return r

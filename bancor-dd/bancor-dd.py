# Use Flask framework
from flask import Flask, render_template, request, session, escape, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Operating system lib
import os

# Database connection and configuration libs
import pyodbc
import urllib

# ------------------------------------
# SET DATABASE CONNECTION
# ------------------------------------
  # Set database connection string
connString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=172.17.97.18;DATABASE=RULES;UID=svcarq;PWD=Arkitectura29'
  # Format connection string
params = urllib.parse.quote_plus(connString)
  # Set database URI
params = "mssql+pyodbc:///?odbc_connect=%s" % params
# ------------------------------------


# Create application object
app = Flask(__name__)

# Set database ORM configuration
app.config["SQLALCHEMY_DATABASE_URI"] = params
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create database object
db = SQLAlchemy(app)


# ------------------------------------
# Create data model entities
# ------------------------------------
class _AuditData ():
    _dateCreated = db.Column(db.DateTime, nullable=False)
    _dateLastUpdated = db.Column(db.DateTime, nullable=True)
    _userCreated = db.Column(db.String(50), nullable=False)
    _userLastUpdated = db.Column(db.String(50), nullable=True)

class CFG_DataComponent (_AuditData, db.Model):
    __tablename__ = 'CFG_DataComponent'
    DataComponentId = db.Column(db.String(20), primary_key=True)
    DataComponentName = db.Column(db.String(255), unique=True, nullable=False)
    DataComponentDescription = db.Column(db.TEXT, nullable=False)
# ------------------------------------


# ------------------------------------
# Create application routes
# ------------------------------------
@app.route("/")
def index():
    DataComponentId = "doc_0000012"
    DataComponent = CFG_DataComponent.query.filter_by(DataComponentId=DataComponentId).first()
    return render_template(
        "index.html", 
        DataComponentId=DataComponent.DataComponentId, 
        DataComponentName=DataComponent.DataComponentName, 
        DataComponentDescription=DataComponent.DataComponentDescription)


@app.route("/listdatacomponents")
def listdatacomponents():
    DataComponents = CFG_DataComponent.query.all()
    return render_template("listdatacomponents.html", DataComponents=DataComponents)

# ------------------------------------


app.secret_key = "12345"


if __name__ == "__main__":
    # db.create_all() To create data objects
    app.run(debug=True, host="0.0.0.0")

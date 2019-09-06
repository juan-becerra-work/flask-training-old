from flask import Flask, render_template, request, session, escape, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
#from classes import db_valuechain
import os

import pyodbc
import urllib


# *************************
# ODBC CONNECTION
# *************************
connString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=172.17.97.18;DATABASE=RULES;UID=svcarq;PWD=Arkitectura29'
cnxn = pyodbc.connect(connString)
cursor = cnxn.cursor()

# cursor.execute("SELECT * FROM dbo.RUL_RULE")
# for row in cursor.fetchall():
#     print (row)
# *************************

#dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

params = urllib.parse.quote_plus(connString)
params = "mssql+pyodbc:///?odbc_connect=%s" % params
#engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
#engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = params
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


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



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    nickname = request.args.get("nickname")

    user = Users.query.filter_by(username=nickname).first()

    if user:
        return user.username

    return "The user doesn't exist."


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        hashed_pw = generate_password_hash(
            request.form["password"], method="sha256")
        new_user = Users(username=request.form["username"], password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        flash("You've registered successfully.", "success")

        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["username"] = user.username
            return "You are logged in"
        flash("Your credentials are invalid, check and try again.", "error")

    return render_template("login.html")


@app.route("/home")
def home():
    if "username" in session:
        return "You are %s" % escape(session["username"])

    return "You must log in first."


@app.route("/logout")
def logout():
    session.pop("username", None)

    return "You are logged out."


app.secret_key = "12345"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="0.0.0.0")

#Imports
from urllib import response
from flask import Flask, render_template, redirect, url_for
from appmodels import create_app
import os
from flask_sqlalchemy import SQLAlchemy, request
import sqlalchemy.orm
from flask_googlemaps import GoogleMaps
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange, Length
from flask_babel import _, lazy_gettext as _l

#Create app using function
app = create_app()
#Create database using SQLAlchemy
db = SQLAlchemy(app)
sessionmaker = sqlalchemy.orm.sessionmaker(db.engine)
# Initialize the extension
GoogleMaps(app)

#Directs user to index page
@app.route("/")
@app.route("/index")
def index():
     return render_template("index.html")

#Directs user to tutorial page
@app.route("/tutorial")
def tutorial():
     return render_template("tutorial.html")

class LocForm(FlaskForm):
    location = StringField(_l('Location'), validators=[DataRequired()])
    submit = SubmitField(_l('Sign In'))

#Directs user to findhhw page, allows users to search a location
@app.route("/findhhw")
def findhhw():
     #form = LocForm()
     #if form.validate_on_submit():
     #     location = form.location.data
     #     return render_template("locatehhw.html", location=location)
     #else:
          return render_template("findhhw.html")

#Displays Google Map to nearest HHW locations based on search
@app.route("/locatehhw")
def locatehhw():
     #Add location bias later
     url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=household%20hazardous%20waste&inputtype=textquery&fields=formatted_address%2Cname%2Cphoto&key=AIzaSyC5wxVkXV3QR6DBt_Rz2-vJ395qU_Prr-I"
     payload={}
     headers = {}

     response = requests.request("GET", url, headers=headers, data=payload)
     return render_template("locatehhw.html", response=response)

if __name__ == "__main__":
  app.run()
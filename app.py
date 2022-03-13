#Imports
from flask import Flask, render_template
from appmodels import create_app
import os
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.orm
from flask_googlemaps import GoogleMaps
import requests

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

#Directs user to findhhw page
@app.route("/findhhw")
def findhhw():
     #Add location bias later
     url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=household%20hazardous%20waste&inputtype=textquery&fields=formatted_address%2Cname%2Cphoto&key=AIzaSyC5wxVkXV3QR6DBt_Rz2-vJ395qU_Prr-I"
     payload={}
     headers = {}

     response = requests.request("GET", url, headers=headers, data=payload)
     return render_template("findhhw.html", response=response)

if __name__ == "__main__":
  app.run()
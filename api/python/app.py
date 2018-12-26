from flask import Flask, request, json, session, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_restful import marshal, fields
from requests.utils import quote
import requests
import datetime
import os
import jwt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abahaos38@localhost:5432/evoting'
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app, support_credentials=True)
db = SQLAlchemy(app)
jwtSecretKey = "companysecret"

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String())

class Paslon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_paslon = db.Column(db.String())
    nomor_paslon = db.Column(db.Integer)
    role_position = db.Column(db.Integer, db.ForeignKey('roles.id'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String())
    full_name = db.Column(db.String())
    NIK = db.Column(db.String())

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_paslon = db.Column(db.String())
    nomor_paslon = db.Column(db.Integer)
    total_vote = db.Column 
   




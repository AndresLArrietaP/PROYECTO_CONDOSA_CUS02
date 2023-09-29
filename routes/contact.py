from flask import Blueprint,request,jsonify
from models.persona import Persona
from utils.db import db

persona=Blueprint('persona',__name__)
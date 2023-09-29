from utils.db import db
from dataclasses import dataclass

@dataclass
class Persona(db.Model):
    id:int
    nombre:str
    apaterno:str
    amaterno:str
    email:str
    direccion:str
    dni:str
    phone:str

    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    apaterno=db.Column(db.String(100))
    amaterno=db.Column(db.String(100))
    email=db.Column(db.String(100))
    direccion=db.Column(db.String(200))
    dni=db.Column(db.String(100))
    phone=db.Column(db.String(100))

    def __init__(self,nombre,apaterno,amaterno,email,direccion,dni,phone):
        self.nombre= nombre
        self.apaterno= apaterno
        self.amaterno= amaterno
        self.email=email
        self.direccion= direccion
        self.dni= dni
        self.phone=phone
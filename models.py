from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumno(db.Model):
    __tablename__ = 'alumnos'
    cuenta = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    primer_apellido = db.Column(db.String(50))
    segundo_apellido = db.Column(db.String(50))
    carrera = db.Column(db.String(50))
    semestre = db.Column(db.Integer)
    promedio = db.Column(db.Float)
    al_corriente = db.Column(db.Boolean)
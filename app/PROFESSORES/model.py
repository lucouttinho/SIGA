from ..extensions import db
from ..Link import link_table

class Professores(db.Model):
    __tablename__ = 'Professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False) 
    cpf = db.Column(db.Integer, unique=True)
    Formacao = db.Column(db.String(20), nullable = False)

    Materia = db.relationship('Materia', secondary = link_table, backref = 'Professores' ) 

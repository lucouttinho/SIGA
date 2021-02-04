from ..extensions import db
from ..Link import link_table

class Turma(db.Model):
    __tablename__ = 'Turma'
    id = db.Column(db.Integer, primary_key=True)
    Horario = db.Column(db.Integer, unique=True)

    Alunos = db.relationship('Alunos', secondary = link_table, backref = 'Turma' )
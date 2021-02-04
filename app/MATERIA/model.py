from ..extensions import db
from ..Link import link_table

class Materia(db.Model):
    __tablename__ = 'Materia'
    id = db.Column(db.Integer, primary_key=True)
    Tipo = db.Column(db.String(20), nullbable=False)

    Professores = db.relationship('Professores', secondary = link_table, backref = 'Materia' ) 

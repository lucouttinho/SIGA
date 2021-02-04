from ..extensions import db
from ..Link import link_table


class Alunos(db.Model):
    __tablename__ = 'Alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False) 
    cpf = db.Column(db.integer, unique=True)
    Periodo = db.Column(db.String(20), nullable=False)
    DataN = db.Column(db.integer, unique=False)
    Curso = db.Column(db.String(20), nullable=False)
    Sexo = db.Column(db.String(20), nullable=False)

    Boletim_id = Column(Integer, ForeignKey('Boletim.id'))
    Boletim = relationship("Boletim", back_populates="Alunos")

     Turma = db.relationship('Turma', secondary = link_table, backref = 'Alunos' ) 


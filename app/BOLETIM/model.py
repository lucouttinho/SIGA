from ..extensions import db

class Boletim(db.Model):
    __tablename__ = 'Boletim'
    id = db.Column(db.Integer, primary_key=True)
    Notas = db.Column(db.Integer,unique=False )
    
    Aluno = relationship("Alunos", uselist=False, back_populates="Boletim")
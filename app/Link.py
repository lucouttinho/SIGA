from .extensions import db

link_table = db.Table('Link', db.Model.metadata,           
                    db.Column('Materia' , db.Integer, db.ForeignKey('Materia.id')),
                    db.Column('Alunos' , db.Integer, db.ForeignKey('Alunos.id')))
                    db.Column('Turma', db.Integer, db.ForeignKey('Turma.id'))
                    db.Column('Professor', db.Integer, db.ForeignKey('Professor.id'))
                    

"""professor.py: create a table named professors in the marist database"""
from db.db import db

class Professor(db.Model):
    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)
    FirstName = db.Column(db.String(55))
    LastName = db.Column(db.String(55))
    Email = db.Column(db.String(55))


    # create relationship with courses table. assoc table name = ProfessorCourse
    course = db.relationship('Courses', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self, FirstName, LastName, Email):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email

    def __repr__(self):
        # add text to the f-string
        return f"Professor(ID={self.ProfessorID}, FirstName='{self.FirstName}', LastName='{self.LastName}', Email='{self.Email}')"
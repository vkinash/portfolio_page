from db_config import db
from flask_login import UserMixin


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    position = db.Column(db.String)
    about = db.Column(db.String)
    birthdate = db.Column(db.DateTime)
    address = db.Column(db.String)
    website_url = db.Column(db.String)
    contacts = db.relationship('Contacts', backref='contacts', lazy=True)
    experience = db.relationship('Experiences', backref='experiences', lazy=True)
    skills = db.relationship('Skills', backref='skills', lazy=True)

    def get_serialize_user_info(self):
        user = {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "position": self.position,
            "about": self.about,
            "birthdate": self.birthdate,
            "address": self.address,
            "website_url": self.website_url,
            "contacts": [c.get_serialize_contacts_info() for c in self.contacts],
            "experience": sorted([e.get_serialize_experiences_info() for e in self.experience], key=lambda x: x["date_to"], reverse=True),
            "skills": [s.get_serialize_skills_info() for s in self.skills]
        }
        return user


class Login(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)
    name = db.Column(db.String)


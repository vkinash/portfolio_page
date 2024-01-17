import datetime

from db_config import db


class Experiences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String)
    company_url = db.Column(db.String)
    company_label = db.Column(db.String)
    position = db.Column(db.String)
    responsibilities = db.Column(db.String)
    date_from = db.Column(db.DateTime)
    date_to = db.Column(db.DateTime)
    address = db.Column(db.String)
    # user = db.relationship('User', backref='user_experience', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def get_serialize_experiences_info(self):
        experience = {
            "id": self.id,
            "company_name": self.company_name,
            "company_url": self.company_url,
            "company_label": self.company_label,
            "position": self.position,
            "responsibilities": [r[2:] for r in self.responsibilities.split("\n")],
            "date_from": datetime.datetime.strftime(self.date_from, "%m.%Y"),
            "date_to": datetime.datetime.strftime(self.date_to, "%m.%Y"),
            # "date_from": self.date_from,
            # "date_to": self.date_to,
            "address": self.address
        }
        return experience
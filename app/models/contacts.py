from db_config import db


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    linkedin_url = db.Column(db.String)
    facebook_url = db.Column(db.String)
    # user = db.relationship('User', backref='user_contacts', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def get_serialize_contacts_info(self):
        contacts = {
            "id": self.id,
            "email": self.email,
            "linkedin_url": self.linkedin_url,
            "facebook_url": self.facebook_url,
            "user_id": self.user_id
        }
        return contacts

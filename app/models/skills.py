from db_config import db


class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    technology = db.Column(db.String, nullable=False)
    # user = db.relationship('User', backref='user_skills', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def get_serialize_skills_info(self):
        skill = {
            "id": self.id,
            "technology": self.technology,
        }
        return skill

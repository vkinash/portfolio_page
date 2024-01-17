import datetime
import time
from flask import jsonify

from app.models.users import User
from app.models.contacts import Contacts
from app.models.skills import Skills
from app.models.experiences import Experiences
from db_config import db
from flask import render_template
from app.edit_forms import EmailForm


def index():
    email_form = EmailForm()
    user = db.session.query(User).join(Contacts).join(Skills).join(Experiences).first()
    if not user:
        return {"error": "User is empty"}
    user = user.get_serialize_user_info()
    birthdate = datetime.datetime.strftime(user["birthdate"], "%m.%d.%Y") if user["birthdate"] else "03.03.1992"
    age = (datetime.datetime.now() - user["birthdate"]).days / 365
    skills = user.get("skills", "No skills")
    contacts = user.get("contacts", "No contacts")
    experiences = user.get("experience", "No experiences")
    return render_template("index.html",
                           about=user["about"],
                           birthdate=birthdate,
                           position=user["position"],
                           email=contacts[0]["email"],
                           age=int(age),
                           address=user["address"],
                           website_url=user["website_url"],
                           contacts=contacts,
                           skills=skills,
                           experiences=experiences,
                           email_form=email_form
                           )


def send_email():
    email_form = EmailForm()
    print(email_form.data)
    return jsonify(success=True, message='Your message has been sent. Thank you.'), 200

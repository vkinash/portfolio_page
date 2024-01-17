import datetime

from app.models.users import User
from app.models.contacts import Contacts
from app.models.skills import Skills
from app.models.experiences import Experiences
from db_config import db
from flask import render_template, redirect, url_for
from app.edit_forms import AboutForm, SkillsForm, ExperienceForm
from flask_login import login_required


@login_required
def edit_profile():
    user = db.session.query(User).join(Contacts).join(Skills).join(Experiences).first()
    if not user:
        return {"error": "User is empty"}
    user = user.get_serialize_user_info()

    about_form = AboutForm()
    skills_form = SkillsForm()
    experience_form = ExperienceForm()

    birthdate = datetime.datetime.strftime(user["birthdate"], "%m.%d.%Y") if user["birthdate"] else "03.03.1992"
    age = (datetime.datetime.now() - user["birthdate"]).days / 365

    skills = user.get("skills", "No skills")
    contacts = user.get("contacts", "No contacts")
    experiences = user.get("experience", "No experiences")
    return render_template("edit.html",
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
                           about_form=about_form,
                           skills_form=skills_form,
                           experience_form=experience_form
                           )


def save_info():
    about_form = AboutForm()
    skills_form = SkillsForm()
    experience_form = ExperienceForm()

    if about_form.about.data:
        db.session.query(User).update({User.about: about_form.data["about"]})

    if about_form.birthdate.data:
        db.session.query(User).update({User.birthdate: about_form.data["birthdate"]})

    if about_form.address.data:
        db.session.query(User).update({User.address: about_form.data["address"]})

    if about_form.website_url.data:
        db.session.query(User).update({User.website_url: about_form.data["website_url"]})

    if about_form.email.data:
        db.session.query(Contacts).update({Contacts.email: about_form.data["email"], Contacts.user_id: 1})

    if skills_form.technology.data:
        new_skills_list = list()
        new_skills = skills_form.data["technology"].split(";")
        for s in new_skills:
            new_skills_list.append(Skills(technology=s, user_id=1))
        db.session.add_all(new_skills_list)

    if experience_form.data:
        experience = Experiences(user_id=1)

        if experience_form.company_name.data:
            experience.company_name = experience_form.data["company_name"]
        if experience_form.position.data:
            experience.position = experience_form.data["position"]
        if experience_form.responsibilities.data:
            experience.responsibilities = experience_form.data["responsibilities"]
        if experience_form.date_from.data:
            experience.date_from = experience_form.data["date_from"]
        if experience_form.date_to.data:
            experience.date_to = experience_form.data["date_to"]
        if experience_form.address.data:
            experience.address = experience_form.data["address"]

        db.session.add(experience)

    db.session.commit()
    return redirect(url_for("edit_page"))

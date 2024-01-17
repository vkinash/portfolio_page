from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length
from app.models.users import User
from db_config import db


class AboutForm(FlaskForm):
    about = TextAreaField('about')
    birthdate = DateField("birthdate")
    address = StringField("address")
    website_url = StringField("website_url")
    email = StringField("email")


class SkillsForm(FlaskForm):
    technology = TextAreaField('technology')


class ExperienceForm(FlaskForm):
    company_name = StringField('company_name')
    company_url = StringField('company_url')
    company_label = StringField('company_label')
    position = StringField('position')
    responsibilities = TextAreaField('responsibilities')
    date_from = DateField("date_from")
    date_to = DateField("date_to")
    address = StringField('address')


class EmailForm(FlaskForm):
    name = StringField("name", render_kw={"class": "form-control", "id": "name"})
    email = StringField("email", render_kw={"class": "form-control", "id": "name"})
    subject = StringField("subject", render_kw={"class": "form-control", "id": "name"})
    message = StringField("message", render_kw={"class": "form-control", "id": "name"})

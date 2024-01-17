from flask import Flask
from db_config import db
from flask_migrate import Migrate
from app.views.index import index, send_email
from app.views.edit import edit_profile, save_info
from app.views.login import login, logout, signup
from flask_login import LoginManager

from app.models.users import User, Login
from app.models.experiences import Experiences
from app.models.contacts import Contacts
from app.models.skills import Skills


def create_app(test_config=None, **kwargs):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
    app.config["SECRET_KEY"] = "secret"

    Migrate(app, db)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    app.add_url_rule("/", view_func=index, methods=["GET"])
    app.add_url_rule("/edit_profile", view_func=edit_profile, methods=["GET"])
    app.add_url_rule("/save_info", view_func=save_info, methods=["POST"])
    app.add_url_rule("/send_email", view_func=send_email, methods=["POST"])
    app.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=logout, methods=["GET"])
    app.add_url_rule("/signup", view_func=signup, methods=["GET", "POST"])

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Login.query.get(int(user_id))

    return app


app = create_app()


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8080", debug=True)
    # create_app().run()

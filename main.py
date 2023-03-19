from os import environ

from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, current_user, logout_user
from flask_restful import Api

from data.db_session import create_session
from data.users import User
from forms import LoginForm
from legacy_api import bp as api_bp
from api import users

app = Flask(__name__)
app.config["SECRET_KEY"] = environ["SECRET_KEY"]
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).get(user_id)


@app.route("/")
def home():
    if current_user.is_authenticated:
        return f"Привет, {current_user.fio}"
    else:
        return "Войдите, пожалуйста :|"


@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect("/")
    return render_template("login.html", form=form)


@app.errorhandler(404)
def not_found_handler(exc):  # exc - ошибка, из-за которой все сломалось
    return "oops, not found this :("


if __name__ == "__main__":
    api.add_resource(users.UsersListResource, "/api/v2/users")
    api.add_resource(users.UsersResource, "/api/v2/users/<int:user_id>")
    app.register_blueprint(api_bp)
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 8080)))

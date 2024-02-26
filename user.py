from flask_login import LoginManager, UserMixin
# from flask import session, redirect, url_for


login_manager = LoginManager()


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

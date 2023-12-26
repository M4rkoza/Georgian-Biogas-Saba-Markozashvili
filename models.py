from ext import database, application, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Product(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    subtext = database.Column(database.String)
    text = database.Column(database.String)
    img = database.Column(database.String)

class Basemodel:
    def create(self):
        database.session.add(self)
        database.session.commit()
    def delete(self):
        database.session.delete(self)
        database.session.commit()

    def save(self):
        database.session.commit()
class User(database.Model, Basemodel,UserMixin):
    __tablename__ = "users"

    id = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String)
    password = database.Column(database.String)
    gender = database.Column(database.String)
    birthday = database.Column(database.DateTime)
    country = database.Column(database.String)
    role = database.Column(database.String)

    def __init__(self, username, password, gender, birthday, country, role="visitor"):
        self.username = username
        self.password = generate_password_hash(password)
        self.gender = gender
        self.birthday = birthday
        self.country = country
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    with application.app_context():
        database.create_all()

        new_user = User(username="SM", password="1sadminm1", role="admin", gender="კაცი", birthday=None, country="საქართველო")
        new_user.create()

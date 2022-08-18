from os import environ, path

# Flask
from flask import Flask, render_template
from flask_security import Security, auth_required, login_required
from flask_restful import Api

# Models
from models import db
from models.users import user_datastore
from models.posts import Posts

# Controllers
from controllers.apis import Posts_Create, Posts_Others, Posts_by_Users, Posts_Fun


# Create app
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "super-secret"
app.config["SECURITY_PASSWORD_SALT"] = "HelloWorld"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config["WTF_CSRF_ENABLED"] = False

# Create database connection object
db.init_app(app)
security = Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
def create_user():
    file_exists = path.exists("database.sqlite3")
    if file_exists != True:
        db.create_all()
        user_datastore.create_user(email="sachin@mail.com", password="root")
        user_datastore.create_user(email="user@mail.com", password="user")
        db.session.commit()


@app.route("/")
# @auth_required()
def index():
    return render_template("index.html")


@auth_required()
def check():
    return "I am working man"


# Apis
api = Api(app)
api.add_resource(Posts_Create, "/api")
api.add_resource(Posts_Others, "/api")
api.add_resource(Posts_Fun, "/api/<post_id>")
api.add_resource(Posts_by_Users, "/api/postbyuser/<id>")

if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0", debug=True)

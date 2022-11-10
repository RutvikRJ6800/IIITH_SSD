from flask import Flask, render_template, session, redirect, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config["SECRET_KEY"] = b'\xcf\xd0\x9b\xb6\xbe\xa1\x90\x91\x8dh\x17\x1d\xbb\xf4C\xe2'

db = SQLAlchemy(app)
# db.init_app(app)
login_manager = LoginManager()

login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email =  db.Column(db.String(80), unique=True, nullable=False)
    password =  db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()
    

@app.route('/')
def home():
    return "Welcome..."

@app.route('/user/signup', methods=['POST'])
def signup():
    if (request.method == 'POST'):
        req = request.get_json()
        print("username:",req["username"])
        print("email:",req["email"])
        print("password:", req["password"])
        newUser = User(username= req["username"], email=req["email"], password=req["password"])
        db.session.add(newUser)
        db.session.commit()
        msg = "Hello user {}. You successfully signedup.".format(req["username"])

        return jsonify({'msg': msg}), 200
    
    else:
        return jsonify({'ERRORR': "Failed to Signup.."}), 401


  
@app.route('/user/signin', methods=['POST'])
def login():
    print("a")
    if (request.method == 'POST'):
        req = request.get_json()
        print("b")
        print("username:",req["username"])

        print("password:", req["password"])
        username = req["username"]
        password = req["password"]

        check_user = User.query.filter_by(username=username).first()
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user)
                msg = "Logged in successfully"
                return jsonify({'msg': msg}), 200 
            else:
                msg = "Incorrect password"
                return jsonify({'msg': msg}), 200
        else:
            msg = "No such User exists"
            return jsonify({'msg': msg}), 200

    else:
        return jsonify({'ERRORR': "Failed to Signup.."}), 401

    
@app.route('/user/signout', methods = ['GET'])
@login_required
def logout():
   logout_user()
   return {"message" : "Loggout successfully"}
 


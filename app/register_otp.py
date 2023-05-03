from flask import Flask,request,Blueprint,jsonify
from flask_sqlalchemy import SQLAlchemy
from app import db,ma

registerotp_bp =Blueprint('register_otp',__name__)

class Registerotp(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(100))
     email = db.Column(db.String(100))
     mobile_number = db.Column(db.String(100))
     password = db.Column(db.String(100))

@registerotp_bp.route('/registerotpd',methods=['POST'])
def registerotp():
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        mobile = data['mobile']
        password = data['password']
        register = Registerotp(name=name,email=email,mobile_number=mobile,password=password)
        db.session.add(register)
        # db.session.commit()
        print(register)
        return "successfully register"
    except Exception as e:
        return str(e)



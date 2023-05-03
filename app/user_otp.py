from flask import Flask,request,Blueprint,jsonify
from flask_sqlalchemy import SQLAlchemy
from app import db,ma
import random
import time
from register_otp import Registerotp
from app import mail
from flask_mail import Mail,Message  #mail send

userotp_bp =Blueprint('user_otp',__name__)


class Userotp(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email =db.Column(db.String(100))
    otp = db.Column(db.Integer)
    exp_time =db.Column(db.Integer)
    user_details=db.Column(db.JSON)

def create_otp():
    otp = random.randint(111111,999999)
    expre_time = int(time.time()) + 300
    return otp,expre_time

@userotp_bp.route('/registerotp',methods=['POST'])
def userOtp():
    data = request.get_json()
    name = data['name']
    email = data['email']
    otp,expre_time = create_otp()
    user = Userotp(email=email,otp=otp,exp_time=expre_time,user_details=data)
    db.session.add(user)
    db.session.commit()
    msg = Message(subject="user registeration otp", recipients=[email],
                      body=f"dear {name.capitalize()} this mail for your Admin-E-commerce user register otp request. And your otp is {otp}.\
                      \n This otp will valid for 5 mins.\nThank You")
    try:
        mail.send(msg)
    except Exception as e:
        print(e)
    return jsonify({"status":"success"})

@userotp_bp.route('/verify_otp',methods=['POST'])
def verify_otp():
    data = request.get_json()
    email = data['email']
    otp = data['otp']
    otp_data = Userotp.query.filter(Userotp.user_details['email'] == email).first()

    if otp_data:
        if int(otp) == otp_data.otp:
            user = Registerotp(name=otp_data.user_details['name'],email=otp_data.user_details['email'],mobile_number=otp_data.user_details['mobile'],password=otp_data.user_details['password'])
            print(user)
            db.session.delete(otp_data)
            db.session.add(user)
            db.session.commit()
            return "success"
    return "falied"


@userotp_bp.route('/resendotp',methods=['POST'])
def resendotp():
    data = request.get_json()
    email = data['email']
    otp,expre_time = create_otp()
    resend_otp = Userotp.query.filter(Userotp.email == email).first()
    resend_otp.otp=otp
    resend_otp.exp_time = expre_time
    db.session.commit()
    msgs = Message(subject="user registeration otp", recipients=[email],
                      body=f"dear this mail for your Admin-E-commerce user register otp request. And your otp is {otp}.\
                      \n This otp will valid for 5 mins.\nThank You")
    try:
        mail.send(msgs)
    except Exception as e:
        print(e)
    return jsonify({"status":"success"})
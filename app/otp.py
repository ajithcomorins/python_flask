from flask import Flask,request,redirect,Blueprint
import os
from twilio.rest import Client
import pyotp
import json

otp_bp = Blueprint('otp',__name__)


account_sid = 'ACfd2546e7ef5e3bafde7e35166a7e12e6'
auth_token = 'aa321840125a07babbb7757900af4daa'
twilio_phone_number = '+1 507 461 8628'
client = Client(account_sid, auth_token)


@otp_bp.route('/genrate_otp',methods=['POST'])
def get_otp():
    data = request.get_json()
    phone_number = data['phone_number']
    totp = pyotp.TOTP(pyotp.random_base32()).now()
    body = f"Your OTP is: {totp} "
    client.messages.create(to=phone_number, from_=twilio_phone_number, body=body)

    return "OTP sent successfully"





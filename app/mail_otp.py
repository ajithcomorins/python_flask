from flask import Flask,request,redirect,Blueprint
from smtplib import SMTP_SSL 
import os   # image path select
import json
from mimetypes import guess_type
from email.message import EmailMessage
from flask_mail import Mail,Message  #mail send

mail_bp =Blueprint('mail_otp',__name__)


file = open('./file.json')
data_file = json.load(file)

SENDER_EMAIL = data_file["email"]
MAIL_PASSWORD = data_file['password']

file_names = ['./upload_img/kumar.jpg','./upload_img/BROCHURE_KARKA.pdf']

def send_attach(SENDER_EMAIL,RECEIVER_EMAIL,MAIL_PASSWORD,subject,content,file_names):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.set_content(content)
    
    for file_name in file_names:
        mime_type, encoding = guess_type(file_name)
        mime_type, sub_type = mime_type.split("/")[0], mime_type.split("/")[1]

        with open(file_name,"rb") as file:
            file_data = file.read()
            msg.add_attachment(
                file_data,otp, maintype=mime_type, subtype=sub_type, filename=file_name
            )
            file.close()
    #sending mail via SMTP Server
    with SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(SENDER_EMAIL,MAIL_PASSWORD)
        smtp.send_message(msg)
        smtp.close()
    return "mail successfully send"
subject = "Multiple Attchment"
content = "file attchment check for this file"


@mail_bp.route('/mail_attach',methods=['POST'])
def mail_attach():
    data = request.get_json()
    RECEIVER_EMAIL = data["mail_id"]
    return send_attach(SENDER_EMAIL,RECEIVER_EMAIL,MAIL_PASSWORD,subject,content,file_names)




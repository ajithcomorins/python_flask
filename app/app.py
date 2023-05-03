from flask import Flask,request,redirect
import os   # image path select
import sys  # stop in line
import json
import schedule
import time
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # table create in database
from datetime import datetime  # sql datetime use
from flask_marshmallow import Marshmallow # json convert
from flask_jwt_extended import get_jwt_identity # token create
from flask_jwt_extended import JWTManager  # token create
from werkzeug.utils import secure_filename # upload file
from flask_mail import Mail,Message  #mail send
from random import *
from flask_cors import CORS # api cors problem solve


app = Flask(__name__)
ma = Marshmallow(app)
mail = Mail(app)
UPLOAD_FOLDER = 'C:/Users/User/Desktop/flask/app/upload_img'
PRODUCT_FOLDER= 'C:/Users/User/Desktop/flask/app/product_image'
# hxdwownxdxhtdled--->password genrate
CORS(app)




app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PRODUCT_FOLDER'] = PRODUCT_FOLDER
app.config['SECRET_KEY'] = 'your_secret_key_here'
file = open('./file.json')
data_file = json.load(file)


# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "ajithkumar260598@gmail.com"
app.config['MAIL_PASSWORD'] = "eqmwndfyfbvoxgnl"
app.config['MAIL_DEFAULT_SENDER'] = "ajithkumar260598@gmail.com"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

db = SQLAlchemy(app)
jwt = JWTManager(app)
# mail = Mail(app) # instantiate the mail class





class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String(100))
    image = db.Column(db.String(100))
    course_type = db.Column(db.String(200))
    datatime= db.Column(db.DateTime,default = datetime.utcnow)
    
class Total_admission(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Total_admission = db.Column(db.String(100))
    datatime= db.Column(db.DateTime,default = datetime.utcnow)

class New_admission(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    batch = db.Column(db.String(100))
    datatime= db.Column(db.DateTime,default = datetime.utcnow)

from chapter import Chapter
from employee import Employee
from multi_insert import User,Post
from product import Product
from image import Photo
from register_otp import Registerotp
from user_otp import Userotp

migrate = Migrate(app,db)


@jwt.user_identity_loader
def user_identity_lookup(emp_id):
    return emp_id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return Employee.query.filter_by(emp_id=identity).one_or_none()

@jwt.user_identity_loader
def user_identity_lookup(id):
    return id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

# todo
class Todoschema(ma.Schema):
    class Meta:
        fields = ('id','task','image','course_type','datatime')
todoschema=Todoschema()



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/',methods=['GET'])
def index():
    return "sqlalchemy"


@app.route('/add',methods=['POST'])
def add():
    try:
        # data = request.get_json()
        add_task = request.form['request']
        course = request.form['course']
        image = request.files['file']
        if image.filename == '':
            return "file is not invalid"
        filename = secure_filename(image.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir,app.config['UPLOAD_FOLDER'],filename))
        todo = Todo(task=add_task,course_type=course,image=filename)
        db.session.add(todo)
        db.session.commit()
        return "success"
    except Exception as e:
      return str(e)

@app.route('/read',methods=['GET'])
def read():
    todo = Todo.query.all()
    result = todoschema.jsonify(todo,many=True)
    return result

@app.route('/update/<id>',methods=['PUT'])
def update(id):
    update = Todo.query.get(id)
    update.task = request.json['task']
    db.session.commit()
    return "status:success"

@app.route('/delete/<id>',methods=['POST'])
def delete(id):
    delete = Todo.query.get(id)
    db.session.delete(delete)
    db.session.commit()
    return "status:success"


#mail send 
@app.route('/mail_otp',methods=['POST'])
def send_mail():
    data = request.get_json()
    receiver_email = data['email']
    msg = Message('flask hello',sender ='ajithkumar260598@gmail.com',recipients = [receiver_email])
    msg.body = 'auto mail mail send--'+ str(otp)
    mail.send(msg)
    return 'Sent successfully'

# schedule.every(10).seconds.do(send_mail)

# def add():
#     try:
#         # data = request.get_json()
#         add_task = request.form['request']
#         image = request.files['file']
#         if image.filename == '':
#             return "file is not invalid"
#         filename = secure_filename(image.filename)
#         basedir = os.path.abspath(os.path.dirname(__file__))
#         image.save(os.path.join(basedir,app.config['UPLOAD_FOLDER'],filename))
#         todo = Todo(task=add_task,image=filename)
#         db.session.add(todo)
#         db.session.commit()
#         return "success"
#     except Exception as e:
#       return str(e)

# @app.route('/course',methods = ['POST'])
# def addCourse():
#     try:
#         data = request.get_json()
#         course = Course(name= data['name'],description = data['description'],slug = data['slug'])
#         db.session.add(course)
#         db.session.flush()
#         if data['chapters']:
#             [course.chapters.append(chap) 
#             for chap_id in data['chapters'] 
#             for chap in LibChapters.query.filter_by(id =chap_id['id']).all()
#             ]
#             db.session.flush()
#         db.session.commit()
#         return Response.success('success',message='course created successfully')
#     except Exception as e:
#         return str(e)


# two table use then New_admission table insert value another Total_admission value decrement count 
@app.route('/new_admission',methods=['POST'])
def new_admission():
    try:
        data = request.get_json()
        name = data['name']
        batch = data['batch']
        new_data = New_admission(name=name,batch=batch)
        total_admission = Total_admission.query.filter_by(id=1).first()
        total_admission.Total_admission=int(total_admission.Total_admission)-1
        db.session.add(new_data,total_admission)
        db.session.commit()
        return "Sucessdata insert"
    except Exception as e:
        return str(e)

@app.route('/admission_delete/<id>',methods=['POST'])
def admission_delete(id):
    try:
        delete = New_admission.query.get(id)
        total_admission = Total_admission.query.filter_by(id=1).first()
        total_admission.Total_admission=int(total_admission.Total_admission)+1
        db.session.delete(delete)
        db.session.commit()
        return "Sucessdata delete"
    except Exception as e:
        return str(e)


from todo import todo_bp
app.register_blueprint(todo_bp)

from chapter import chapter_bp
app.register_blueprint(chapter_bp)

from employee import employee_bp
app.register_blueprint(employee_bp)

from mail import mail_bp
app.register_blueprint(mail_bp)

from otp import otp_bp
app.register_blueprint(otp_bp)

from multi_insert import multiinsert_bp
app.register_blueprint(multiinsert_bp)

from product import product_bp
app.register_blueprint(product_bp)

from image import image_bp
app.register_blueprint(image_bp)


from register_otp import registerotp_bp
app.register_blueprint(registerotp_bp)


from user_otp import userotp_bp
app.register_blueprint(userotp_bp)

# with app.app_context():
    # schedule.every().day.at("10:00").do(send_mail)
    # schedule.every(30).seconds.do(send_mail)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    

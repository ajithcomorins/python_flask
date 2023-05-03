from flask import Flask,request,Blueprint,jsonify
from flask_sqlalchemy import SQLAlchemy
from app import db,ma
from passlib.hash import sha256_crypt
from flask_jwt_extended import create_access_token # login token create
from flask_jwt_extended import jwt_required # token create then current_user id get
from flask_jwt_extended import current_user # token create then current_user id get

multiinsert_bp =Blueprint('multiinsert',__name__)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(100))
    
    posts = db.relationship('Post', backref='user', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  


class Userchema(ma.Schema):
    class Meta:
        fields = ('id','name','email')
userchema=Userchema()

class Postchema(ma.Schema):
    class Meta:
        fields = ('id','title','content','user_id')
postchema=Postchema()


@multiinsert_bp.route('/multi_add',methods=['POST'])
def multitable():
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        password = sha256_crypt.encrypt(data['password'])
        title = data['title']
        content = data['content']

        user = User(name=name, email=email,password=password)
        db.session.add(user)
        db.session.commit()

        post = Post(title=title, content=content, user_id=user.id)
        db.session.add(post)
        db.session.commit()

        return 'Data added successfully'
    except Exception as e:
        return str(e)


@multiinsert_bp.route('/multi_read',methods=['GET'])
def multi_read():
    try:
        multi_read = Post.query.all()
        result = postchema.jsonify(multi_read,many=True)
        return result
    except Exception as e:
      return str(e)

@multiinsert_bp.route('/multi_login',methods=['POST'])
def multi_login():
    try:
        data = request.get_json()
        login_name = data['name']
        login_password = data['password']
        user = User.query.filter_by(name=login_name).first()

        if not user:
            return "Invalid credentials"

        if not sha256_crypt.verify(login_password,user.password):
            return "Invalid credentials"

        # if user:
        #     # access_token = create_access_token(identity=user.id)
        #     return "success"
        print(user.name)
        return jsonify({"status":"success","data":userchema.dump(user)})
    except Exception as e:
        return str(e)


@multiinsert_bp.route('/current_id',methods=['GET'])
@jwt_required()
def protected():
    return jsonify(current_user.id)



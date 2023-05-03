# from flask import Flask,request,Blueprint,jsonify
# from flask_sqlalchemy import SQLAlchemy
# import json
# import os   # image path select
# from app import db,ma,app
# from werkzeug.utils import secure_filename # upload file

# product_bp=Blueprint('product',__name__)


# UPLOAD_FOLDER = 'C:/Users/User/Desktop/flask/app/product_image'

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     category = db.Column(db.String(100))
#     title = db.Column(db.String(100))
#     description = db.Column(db.String(200))
#     price = db.Column(db.String(100))
#     image = db.Column(db.String(200))


# class Productchema(ma.Schema):
#     class Meta:
#         fields = ('id','categoty','title','description','price','image')
# productchema=Productchema() 


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @product_bp.route('/product_add',methods=['POST'])
# def product_add():
#     try:
#         # data = request.get_json()
#         category = request.form['category']
#         title = request.form['title']
#         description = request.form['description']
#         price = request.form['price']
#         image = request.files['image']
#         if image.filename == '':
#             return "Invaild data"
#         filename = secure_filename(image.filename)
#         basedir = os.path.abspath(os.path.dirname(__file__))
#         image.save(os.path.join(basedir,app.config['PRODUCT_FOLDER'],filename))
#         product = Product(category=category,title=title,description=description,price=price,image=filename)
#         db.session.add(product)
#         db.session.commit()
#         return "sucessfully"
#     except Exception as e:
#         return str(e)


# @product_bp.route('/product_read',methods=['GET'])
# def product_read():
#     product_read = Product.query.all()
#     result = productchema.jsonify(product_read,many=True)
#     return result
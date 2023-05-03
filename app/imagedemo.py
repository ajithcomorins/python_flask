# from flask import Flask,request,Blueprint,jsonify,Response
# from flask_sqlalchemy import SQLAlchemy
# import json
# import os   # image path select
# from app import db,ma,app
# from werkzeug.utils import secure_filename # upload file
# import base64

# product_bp=Blueprint('product',__name__)


# UPLOAD_FOLDER = 'C:/Users/User/Desktop/flask/app/product_image'

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     category = db.Column(db.String(100))
#     title = db.Column(db.String(100))
#     description = db.Column(db.String(200))
#     price = db.Column(db.String(100))
#     image = db.Column(db.LargeBinary)
#     pic_name = db.Column(db.String(200),nullable=True)
#     mimetype = db.Column(db.String(200),nullable=True)

# class Productchema(ma.Schema):
#     class Meta:
#         fields = ('id','category','title','description','price','image','mimetype','pic_name')
# productchema=Productchema() 


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# @product_bp.route('/product_add',methods=['POST'])
# def product_add():
#     try:
#         if request.files:
#             file = request.files['image']
#             category = request.form['category']
#             title = request.form['title']
#             description = request.form['description']
#             price = request.form['price']
#             image = file.read()
#             pic_name = file.filename
#             # if file.filename == '':
#             #     return "Invaild data"
#             # filename = secure_filename(file.filename)
#             mimetype = file.mimetype
#             # basedir = os.path.abspath(os.path.dirname(__file__))
#             # file.save(os.path.join(basedir,app.config['PRODUCT_FOLDER'],filename))
#             product = Product(category=category,title=title,description=description,price=price,image=image,mimetype=mimetype,pic_name=pic_name)
#             db.session.add(product)
#             db.session.commit()
#         else:
#             category = request.form['category']
#             title = request.form['title']
#             description = request.form['description']
#             price = request.form['price']
#             image = request.form['image']
#             product = Product(category=category,title=title,description=description,price=price,image=image,mimetype='null',pic_name='null')
#             print(product)
#             db.session.add(product)
#             db.session.commit()
#         return "sucessfully"
#     except Exception as e:
#         return str(e)


# @product_bp.route('/product_read',methods=['GET'])
# def product_read():
#     product_read = Product.query.all()
#     product_list = []
#     for product in product_read:
#         product_dict = Response({'id': product.id, 'category':product.category,'title':product.title,'description':product.description,'price': product.price,'image': base64.b64encode(product.image).decode(),'mimetype': product.mimetype,'price':product.price,'pic_name': product.pic_name,})
#         product_list.append(product_dict)
#     return {'products': product_list}

  

# # @product_bp('/images_read')
# # def get_images():
# #   images = product.query.all()
# #   image_list = []
# #   for image in images:
# #     image_dict = {'id': image.id, 'name': image.name, 'data': image.data}
# #     image_list.append(image_dict)
# #   return {'images': image_list}
